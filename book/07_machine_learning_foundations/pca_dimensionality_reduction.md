# PCA and Dimensionality Reduction (Deep Dive)

📄 File: `book/07_machine_learning_foundations/pca_dimensionality_reduction.md`

This chapter covers **PCA** — reduce dimensions while preserving variance. Essential for visualization and feature engineering.

---

## Study Plan (2–3 days)

* Day 1: Variance, covariance
* Day 2: PCA algorithm
* Day 3: Use cases, exercises

---

## 1 — Why Dimensionality Reduction?

* **Visualization**: 2D/3D from high-D
* **Noise reduction**: Remove low-variance components
* **Speed**: Fewer features → faster models

```mermaid
flowchart LR
    A[High-D Data] --> B[PCA]
    B --> C[Low-D Representation]
```

---

## 2 — PCA Idea

* Find **principal components** (directions of max variance)
* Project data onto top K components
* Preserve most variance with fewer dimensions

---

## 3 — PCA with sklearn

```python
from sklearn.decomposition import PCA

# n_components: number of dimensions to keep
pca = PCA(n_components=2)

# Fit: compute principal components from data
pca.fit(X)

# Transform: project data to new space
X_reduced = pca.transform(X)

# Explained variance ratio: % variance per component
print(pca.explained_variance_ratio_)
```

---

## 4 — Steps (Conceptual)

1. **Center** data (subtract mean)
2. **Covariance matrix** of features
3. **Eigenvectors** of covariance = principal components
4. **Project** onto top K eigenvectors

---

## 5 — Why PCA for AI Data Engineering?

* **Embeddings**: Reduce embedding dimension
* **Visualization**: Plot high-D data
* **Preprocessing**: Denoise before model

---

## Interview Questions

1. What does PCA preserve?
2. When to use PCA vs t-SNE?
3. PCA assumptions?

---

## Key Takeaways

* PCA = linear projection to max variance directions
* Reduces dimensions, preserves variance
* Center data first

---

## Next Chapter

You've completed **ML Foundations**. Proceed to: **08_deep_learning**
