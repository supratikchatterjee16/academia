# PyTorch Lightning

**Lightning** (formerly *PyTorch Lightning*) is a deep learning framework that structures PyTorch code to:

* **Remove engineering boilerplate**
* **Scale seamlessly** (multi-GPU, TPU, distributed)
* **Maintain full PyTorch flexibility**

It wraps your PyTorch logic inside a modular, clean interface—letting you focus on research and experimentation instead of boilerplate loops.

---

## Common Use Cases

* Rapid prototyping of PyTorch models
* Large-scale model training (multi-GPU/TPU)
* Mixed precision and distributed training
* Reproducible experimentation
* Integration with logging frameworks (TensorBoard, MLflow, WandB)
* Model checkpointing and deployment

---

## `LightningModule`

A `LightningModule` is the **core abstraction**.
It subclasses `nn.Module` and defines:

* Model architecture
* Training, validation, and test logic
* Optimizers and schedulers
* Metrics and logging

```python
import lightning as L
from torch import nn, optim

class LitAutoEncoder(L.LightningModule):
    def __init__(self, encoder, decoder):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder

    def training_step(self, batch, batch_idx):
        x, _ = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = nn.functional.mse_loss(x_hat, x)
        self.log("train_loss", loss)
        return loss

    def configure_optimizers(self):
        return optim.Adam(self.parameters(), lr=1e-3)
```

---

## Core Methods You Can Override in `LightningModule`

| **Method**                                                        | **Purpose**                                                                      |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `forward(batch)`                                                  | Defines how input data flows through your model. Used for inference and testing. |
| `training_step(batch, batch_idx)`                                 | Defines the per-batch logic for training (computes loss, logs metrics).          |
| `validation_step(batch, batch_idx)`                               | Defines logic for validation runs.                                               |
| `test_step(batch, batch_idx)`                                     | Defines logic for testing.                                                       |
| `predict_step(batch, batch_idx)`                                  | Used during prediction/inference loops.                                          |
| `configure_optimizers()`                                          | Returns one or more optimizers (and optionally LR schedulers).                   |
| `on_train_start() / on_train_end()`                               | Hooks for setup/teardown at the start/end of training.                           |
| `on_epoch_start() / on_epoch_end()`                               | Called at the start/end of every epoch.                                          |
| `on_validation_epoch_end()`                                       | Hook for epoch-level validation logic.                                           |
| `backward(loss)`                                                  | Customizes backward pass (rarely needed, but supported).                         |
| `optimizer_step(epoch, batch_idx, optimizer, optimizer_idx, ...)` | Override for custom optimization behavior.                                       |

> Lightning offers **20+ hooks** for complete control if needed, without writing your own loops.

---

## Typical Workflow

1. **Define** the `LightningModule`
2. **Prepare** datasets and dataloaders
3. **Train** using `Trainer.fit()`
4. **Evaluate or predict** using `Trainer.validate()` / `Trainer.predict()`
5. **Export or deploy** using TorchScript, ONNX, or integrated serving tools

---

## Integration with FastAPI

### Why integrate?

FastAPI is a high-performance web framework for serving machine learning models. Combining it with Lightning allows:

* **Serving trained models as APIs**
* **Real-time inference**
* **Clean separation** between training (Lightning) and deployment (FastAPI)
* **Automatic scalability** using FastAPI workers and Lightning checkpoints

### Example Integration

```python
# fastapi_app.py
from fastapi import FastAPI
from pydantic import BaseModel
import torch
from model import LitAutoEncoder  # your Lightning model

app = FastAPI()

# Load trained model
model = LitAutoEncoder.load_from_checkpoint("path/to/checkpoint.ckpt")
model.eval()

class InputData(BaseModel):
    data: list[float]

@app.post("/predict")
def predict(input: InputData):
    x = torch.tensor(input.data).unsqueeze(0)
    with torch.no_grad():
        z = model.encoder(x)
    return {"embedding": z.tolist()}
```

Then run:

```bash
uvicorn fastapi_app:app --reload
```

This setup allows you to:

* Train with Lightning on powerful clusters
* Export checkpoints
* Serve those models through FastAPI REST endpoints for production inference
