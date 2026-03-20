# JAX Basics

📄 File: `book/08_deep_learning/jax_basics.md`

This chapter covers **JAX** — a high-performance numerical computing library from Google. JAX powers research at DeepMind and Google Brain. AI data engineers encounter it when supporting training pipelines or optimizing numerical code.

---

## Study Plan (2–3 days)

* Day 1: JAX arrays + JIT + autograd
* Day 2: vmap + pmap + Flax basics
* Day 3: PyTorch vs JAX + exercises

---

## 1 — What is JAX?

JAX is **NumPy on accelerators** with automatic differentiation and JIT compilation.

* **Functional** — Pure functions; no mutable state
* **JIT** — `jax.jit` compiles to XLA for CPU/GPU/TPU
* **Autodiff** — `grad`, `jacfwd`, `jacrev` for derivatives
* **Vectorization** — `vmap` for batch parallelism; `pmap` for device parallelism

---

## 2 — JAX Arrays (DeviceArray)

```python
import jax.numpy as jnp

# Create arrays (similar to NumPy)
x = jnp.array([1.0, 2.0, 3.0])
y = jnp.zeros((2, 3))
z = jnp.ones((2, 3))
r = jnp.random.normal(key=jax.random.PRNGKey(0), shape=(2, 3))

# Operations
a = jnp.array([[1.0, 2.0], [3.0, 4.0]])
b = a @ a  # matrix multiply
c = jnp.sum(a, axis=1)
```

### Key difference: PRNG

JAX uses **explicit random keys** — no global state.

```python
import jax.random as jr

key = jr.PRNGKey(42)
key, subkey = jr.split(key)
x = jr.normal(subkey, (3, 3))
```

---

## 3 — JIT Compilation

`jax.jit` compiles a function to XLA for fast execution.

```python
import jax

def f(x):
    return jnp.sum(x ** 2)

f_jit = jax.jit(f)

# First call: compile (slow)
result = f_jit(jnp.ones(1000))

# Later calls: use cached compilation (fast)
result = f_jit(jnp.ones(1000))
```

### When JIT helps

* Loops over arrays
* Repeated small operations
* Functions called many times with same shapes

### When JIT does not help

* Dynamic shapes (recompiles each time)
* Python control flow that depends on data
* Very small functions (overhead dominates)

---

## 4 — Automatic Differentiation

```python
from jax import grad

def loss(w, x, y):
    return jnp.sum((jnp.dot(x, w) - y) ** 2)

grad_loss = grad(loss, argnums=0)  # gradient w.r.t. first arg (w)
g = grad_loss(w, x, y)
```

### Higher-order derivatives

```python
hessian = jax.hessian(loss)
jacobian = jax.jacfwd(f)  # or jacrev
```

---

## 5 — vmap (Vectorization)

`vmap` maps a function over batch dimensions — no explicit loops.

```python
def f(x):
    return jnp.sum(x ** 2)

# Apply f to each row
f_batched = jax.vmap(f)
result = f_batched(jnp.ones(100, 10))  # shape (100,)
```

### Example: batch matrix multiply

```python
# Without vmap: manual loop
# With vmap: vectorized
batch_matmul = jax.vmap(jnp.dot)
```

---

## 6 — pmap (Parallel Map)

`pmap` runs a function in parallel across multiple devices (GPUs/TPUs).

```python
# Replicate data across devices and run in parallel
f_parallel = jax.pmap(f)
result = f_parallel(x_sharded)  # x_sharded has leading device dimension
```

---

## 7 — Flax (Neural Networks)

Flax is the standard NN library for JAX.

```python
import flax.linen as nn

class MLP(nn.Module):
    hidden_dim: int
    out_dim: int

    @nn.compact
    def __call__(self, x):
        x = nn.Dense(self.hidden_dim)(x)
        x = nn.relu(x)
        x = nn.Dense(self.out_dim)(x)
        return x

model = MLP(hidden_dim=256, out_dim=10)
params = model.init(jr.PRNGKey(0), jnp.ones(1, 784))["params"]
output = model.apply({"params": params}, x)
```

---

## 8 — PyTorch vs JAX

| Aspect | PyTorch | JAX |
| ------ | ------- | ----- |
| **Style** | Imperative, define-by-run | Functional, pure functions |
| **Random** | Global state | Explicit PRNG keys |
| **Compilation** | Optional (torch.compile) | JIT by default |
| **Device** | Explicit .to(device) | Automatic; pmap for multi-device |
| **Ecosystem** | Larger (vision, NLP) | Growing (Flax, Equinox) |
| **Used by** | Meta, many startups | Google, DeepMind |

### When to use which

* **PyTorch** — Most teams, production, broad ecosystem
* **JAX** — Research at Google/DeepMind, TPU workloads, functional style preference

---

## Exercises

### 1. Implement gradient descent with JAX

Minimize `f(x) = x^2` using `grad`. Start at `x = 5.0`, run 10 steps.

### 2. JIT a simple function

Write a function that computes the mean of squared values. Compare timing with and without `jax.jit`.

### 3. Use vmap for batch processing

Apply a linear transformation `y = Wx + b` to a batch of 32 vectors using `vmap`.

---

## Interview Questions

1. **Why does JAX use explicit random keys?**
   * Answer: Reproducibility and parallelism. No global state; keys can be split for parallel RNG.

2. **What is the difference between vmap and pmap?**
   * Answer: `vmap` vectorizes over a batch dimension on one device; `pmap` runs in parallel across multiple devices.

3. **When would you choose JAX over PyTorch?**
   * Answer: TPU workloads, functional programming preference, research at Google/DeepMind, or need for JIT by default.

---

## Key Takeaways

* **JAX** — NumPy + autodiff + JIT; functional, no mutable state
* **JIT** — `jax.jit` compiles to XLA for speed
* **Gradients** — `grad`, `jacfwd`, `jacrev`
* **vmap** — Batch parallelism; **pmap** — device parallelism
* **Flax** — Standard NN library for JAX

---

## Next Chapter

Proceed to:

**PyTorch Basics** — `book/08_deep_learning/pytorch_basics.md`

Or **Training Loops** — `book/08_deep_learning/training_loops.md`
