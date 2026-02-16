"""
PINN package — Physics-Informed Neural Networks for Seismic RC Prediction.

Modules
-------
model             : HybridPINN architecture (1D-CNN encoder + FC head).
loss              : Three-component hybrid loss (L_data + L_physics + L_bc).
trainer           : Training loop with AdamW, cosine annealing, early stopping.
benchmark_latency : Inference latency benchmarking for real-time validation.
"""

from src.pinn.loss import HybridPINNLoss, LossWeights
from src.pinn.model import HybridPINN, PINNConfig, build_pinn
from src.pinn.trainer import PINNTrainer, TrainConfig

__all__ = [
    "HybridPINN",
    "PINNConfig",
    "build_pinn",
    "HybridPINNLoss",
    "LossWeights",
    "PINNTrainer",
    "TrainConfig",
]
