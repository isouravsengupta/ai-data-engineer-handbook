# PyTorch Basics

📄 File: `book/08_deep_learning/pytorch_basics.md`

This chapter covers **PyTorch fundamentals** — the dominant framework for deep learning research and production. AI data engineers need to understand tensors, autograd, and the training loop to support model development and debugging.

---

## Study Plan (3–4 days)

* Day 1: Tensors + operations + device management
* Day 2: Autograd + nn.Module + loss and optimization
* Day 3: Training loop + GPU usage + common patterns
* Day 4: Exercises + mini project

---

## 1 — What is PyTorch?

PyTorch is a **tensor computation library** with automatic differentiation. It powers most modern AI research and many production systems.

* **Imperative** — Define-by-run; graphs are built as you execute
* **Pythonic** — Feels like NumPy with GPU support
* **Autograd** — Automatic gradient computation for backpropagation

---

## 2 — Tensors

Tensors are multi-dimensional arrays. They are the core data structure in PyTorch.

```python
import torch

# Create tensors
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.zeros(2, 3)
z = torch.ones(2, 3)
r = torch.randn(2, 3)  # random normal

# Shape and dtype
print(x.shape)   # torch.Size([3])
print(x.dtype)   # torch.float32
```

### Tensor operations

```python
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

# Element-wise
c = a + b
d = a * b

# Matrix multiply
e = torch.mm(a, b)   # or a @ b

# Reshape
f = a.view(4)        # flatten
g = a.reshape(1, 4)
```

### Device: CPU vs GPU

```python
# Move to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.randn(1000, 1000, device=device)

# Or create directly on device
y = torch.randn(1000, 1000).to(device)
```

---

## 3 — Autograd (Automatic Differentiation)

PyTorch tracks operations on tensors and computes gradients automatically.

```python
x = torch.tensor([2.0], requires_grad=True)
y = x ** 2
y.backward()
print(x.grad)  # dy/dx = 2x = 4.0
```

### Gradient flow

```python
w = torch.tensor([1.0], requires_grad=True)
b = torch.tensor([0.0], requires_grad=True)
x = torch.tensor([3.0])

# Forward
y = w * x + b
loss = (y - 5.0) ** 2

# Backward
loss.backward()
print(w.grad)  # gradient w.r.t. w
print(b.grad)  # gradient w.r.t. b
```

### Important: `no_grad()` for inference

```python
model.eval()
with torch.no_grad():
    output = model(input_tensor)  # no gradient tracking, saves memory
```

---

## 4 — nn.Module and Layers

`nn.Module` is the base class for all neural network components.

```python
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 256)
        self.fc2 = nn.Linear(256, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = SimpleNet()
```

### Common layers

| Layer | Purpose |
| ----- | ------- |
| `nn.Linear(in, out)` | Fully connected |
| `nn.Conv2d(in, out, k)` | 2D convolution |
| `nn.ReLU()` | Activation |
| `nn.Dropout(p)` | Regularization |
| `nn.BatchNorm2d(c)` | Normalization |

---

## 5 — Loss and Optimizer

```python
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# Training step
optimizer.zero_grad()
output = model(x)
loss = criterion(output, target)
loss.backward()
optimizer.step()
```

### Why `zero_grad()`?

Gradients accumulate by default. You must zero them before each backward pass.

---

## 6 — Training Loop (Minimal)

```python
model.train()
for epoch in range(num_epochs):
    for x_batch, y_batch in dataloader:
        x_batch, y_batch = x_batch.to(device), y_batch.to(device)
        optimizer.zero_grad()
        output = model(x_batch)
        loss = criterion(output, y_batch)
        loss.backward()
        optimizer.step()
```

---

## 7 — DataLoader

```python
from torch.utils.data import DataLoader, TensorDataset

dataset = TensorDataset(x_tensor, y_tensor)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=4)

for batch_x, batch_y in dataloader:
    # batch_x shape: (32, ...)
    pass
```

---

## 8 — Save and Load

```python
# Save
torch.save(model.state_dict(), "model.pt")

# Load
model.load_state_dict(torch.load("model.pt"))
```

---

## Exercises

### 1. Implement a linear regression with autograd

Fit `y = 2x + 1` using gradient descent. Use `requires_grad=True` on parameters.

### 2. Build a 2-layer MLP for MNIST

Use `nn.Linear`, `nn.ReLU`, `nn.CrossEntropyLoss`. Train for 2 epochs.

### 3. Move a model to GPU

Create a small model, move it and sample data to CUDA, run one forward pass.

---

## Interview Questions

1. **What is the difference between `view` and `reshape`?**
   * Answer: `view` requires contiguous memory; `reshape` may return a copy. `view` is faster when valid.

2. **Why use `torch.no_grad()` during inference?**
   * Answer: Disables gradient tracking, saving memory and compute. Gradients are not needed for inference.

3. **What does `optimizer.zero_grad()` do?**
   * Answer: Zeros the gradients. PyTorch accumulates gradients; without zeroing, gradients from previous steps would add up.

4. **When would you use `model.eval()`?**
   * Answer: During inference or validation. Disables dropout and changes BatchNorm to use running stats.

---

## Key Takeaways

* **Tensors** — Core data structure; support CPU/GPU, autograd
* **Autograd** — Gradients computed automatically via `backward()`
* **nn.Module** — Base for layers and models; define `forward()`
* **Training loop** — zero_grad → forward → loss → backward → step
* **Device** — Use `.to(device)` for GPU; `no_grad()` for inference

---

## Next Chapter

Proceed to:

**JAX Basics** — `book/08_deep_learning/jax_basics.md`

Or **Training Loops** — `book/08_deep_learning/training_loops.md`
