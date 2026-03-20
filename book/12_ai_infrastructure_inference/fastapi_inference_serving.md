# FastAPI for Inference Serving

📄 File: `book/12_ai_infrastructure_inference/fastapi_inference_serving.md`

This chapter covers **FastAPI** as the API layer for AI inference. vLLM, Triton, and Ray Serve handle model execution; FastAPI exposes them as HTTP endpoints. AI data engineers use FastAPI to build production inference APIs.

---

## Study Plan (2 days)

* Day 1: FastAPI basics + async + request/response models
* Day 2: Integrate with vLLM/Ray Serve + deployment with uvicorn

---

## 1 — Why FastAPI for Inference?

* **Async** — Non-blocking I/O; handles many concurrent requests
* **Fast** — One of the fastest Python web frameworks
* **Typed** — Pydantic models for validation and docs
* **OpenAPI** — Auto-generated Swagger UI for testing

---

## 2 — Minimal FastAPI App

```python
from fastapi import FastAPI

# Create FastAPI app with metadata for OpenAPI docs
app = FastAPI(title="Inference API", version="1.0.0")

@app.get("/health")
def health():
    # Health check for load balancers and k8s probes
    return {"status": "ok"}

@app.post("/predict")
def predict(text: str):
    # Placeholder: replace with model call
    return {"prediction": text[:10]}
```

```mermaid
flowchart LR
    A[Client] --> B[FastAPI]
    B --> C[/health]
    B --> D[/predict]
```

### Run with uvicorn

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 3 — Request and Response Models

Use Pydantic for validation and documentation.

```python
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

# Request schema — validated automatically
class PredictRequest(BaseModel):
    text: str
    max_tokens: int = 100  # Default if not provided

# Response schema — ensures consistent output shape
class PredictResponse(BaseModel):
    prediction: str
    tokens_used: int

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    # req is validated; invalid JSON returns 422
    result = model.generate(req.text, max_tokens=req.max_tokens)
    return PredictResponse(prediction=result.text, tokens_used=result.tokens)
```

---

## 4 — Async Endpoints

Use `async def` for non-blocking I/O. Critical when the model runs on a separate process or you call external APIs.

```python
@app.post("/predict")
async def predict(req: PredictRequest):
    # Async allows other requests to be handled while waiting
    result = await model_client.generate_async(req.text)
    return {"prediction": result}
```

### When to use async

* Calling external APIs (OpenAI, embeddings)
* Waiting on Ray Serve / vLLM (if they expose async clients)
* Database or cache lookups

---

## 5 — Integrating with vLLM

vLLM exposes an OpenAI-compatible API. You can proxy it or wrap it in FastAPI for custom logic.

```python
from fastapi import FastAPI
from openai import AsyncOpenAI  # vLLM is OpenAI-compatible

app = FastAPI()
client = AsyncOpenAI(base_url="http://localhost:8000/v1", api_key="dummy")

@app.post("/chat")
async def chat(messages: list[dict]):
    response = await client.chat.completions.create(
        model="meta-llama/Llama-2-7b",
        messages=messages,
        max_tokens=256,
    )
    return {"content": response.choices[0].message.content}
```

---

## 6 — Integrating with Ray Serve

Ray Serve deployments can be called from FastAPI.

```python
from fastapi import FastAPI
from ray import serve

app = FastAPI()

@serve.deployment
class ModelDeployment:
    def __init__(self):
        self.model = load_model()

    def __call__(self, request: dict):
        return self.model.generate(request["text"])

# In production, get handle from Ray Serve
# model_handle = serve.get_deployment_handle("ModelDeployment", "default")

@app.post("/predict")
async def predict(text: str):
    # model_handle.remote({"text": text})
    return {"prediction": "placeholder"}
```

---

## 7 — Streaming Responses

For LLM token streaming, use `StreamingResponse`.

```python
from fastapi.responses import StreamingResponse

async def generate_tokens(prompt: str):
    async for token in model.stream(prompt):
        yield f"data: {token}\n\n"

@app.post("/stream")
async def stream(prompt: str):
    return StreamingResponse(
        generate_tokens(prompt),
        media_type="text/event-stream",
    )
```

---

## 8 — Error Handling

```python
from fastapi import HTTPException

@app.post("/predict")
async def predict(req: PredictRequest):
    if len(req.text) > 10000:
        raise HTTPException(status_code=400, detail="Text too long")
    try:
        return await model.generate(req.text)
    except ModelTimeoutError:
        raise HTTPException(status_code=504, detail="Model timeout")
```

---

## 9 — Deployment

### uvicorn (development and small production)

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Gunicorn + uvicorn workers (production)

```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Exercises

### 1. Build a minimal inference API

Create a FastAPI app with `/health` and `/predict`. Use a dummy model (echo input) or a small Hugging Face model.

### 2. Add request validation

Define a Pydantic model for `/predict` with `text`, `max_tokens`, and `temperature`. Reject invalid values.

### 3. Add streaming

Implement a `/stream` endpoint that yields tokens one at a time using `StreamingResponse`.

---

## Interview Questions

1. **Why use FastAPI over Flask for inference?**
   * Answer: Async support, better performance, automatic OpenAPI docs, Pydantic validation. Inference often involves I/O-bound waits.

2. **What is the role of uvicorn?**
   * Answer: ASGI server that runs FastAPI. Handles async, multiple workers, and production deployment.

3. **When would you use StreamingResponse?**
   * Answer: LLM token streaming — reduces time-to-first-token and improves perceived latency for chat interfaces.

---

## Key Takeaways

* **FastAPI** — Async, typed, fast; ideal API layer for inference
* **Pydantic** — Request/response validation and docs
* **Async** — Use for I/O-bound model calls and external APIs
* **Streaming** — `StreamingResponse` for token-by-token LLM output
* **Deploy** — uvicorn or gunicorn + uvicorn workers

---

## Next Chapter

Proceed to:

**vLLM** — `book/12_ai_infrastructure_inference/vllm.md`

Or **Ray Serve** — `book/12_ai_infrastructure_inference/ray_serve.md`
