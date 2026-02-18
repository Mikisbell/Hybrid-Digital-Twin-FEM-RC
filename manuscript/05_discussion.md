# 5. Discussion

## 5.1 Interpretation of Results

The Hybrid PINN demonstrated strong predictive capability ($R^2 = 0.803$) on unseen ground motions, despite being trained on a relatively small dataset of 20 synthetic records. This efficiency is attributed to the physics-based regularization term ($L_{phy}$), which constrained the search space to physically valid solutions, acting as an inductive bias that substitutes for massive data requirements typical of pure data-driven deep learning.

The breakdown of accuracy by story level reveals that the model captures the fundamental mode response well (Story 1 $R^2=0.84$), but struggles slightly with higher-mode effects in the upper stories (Story 5 $R^2=0.69$). This is consistent with the spectral characteristics of the ground motions, which were scaled to a design spectrum that may not fully excite the higher modes of the frame.

## 5.2 Comparison with Methods

Unlike traditional finite element models (FEM) that require seconds to minutes for nonlinear time history analysis, the proposed surrogate model achieves similar accuracy with sub-millisecond latency. Compared to pure "black-box" data-driven models (e.g., standard LSTMs), the physics-informed approach offers greater interpretability and robustness, as the outputs are guaranteed to be closer to satisfying the equation of motion, reducing the risk of non-physical predictions.

## 5.3 Practical Implications

The benchmarking results (Section 4.5) confirm that the model's inference time (~1 ms) is negligible compared to the typical sampling rate of structural health monitoring sensors (50-100 Hz, i.e., 10-20 ms period). This enables:
1.  **Real-Time Damage Assessment**: Immediate post-earthquake evaluation of drift demands.
2.  **Structural Control**: The potential to drive semi-active dampers or actuators with minimal lag.
3.  **Low-Cost Edge Deployment**: The CPU-based performance suggests feasibility on edge devices (like Raspberry Pi) without needing expensive GPUs.

## 5.4 Limitations

1.  **Dataset Size**: The current study used 20 synthetic records. A larger suite of real PEER records is needed to generalize across a wider range of seismic intensities and frequency contents.
2.  **Model Complexity**: The 2D frame model ignores torsional effects and bidirectional ground motion components present in real 3D structures.
3.  **Material Models**: The OpenSeesPy model assumes perfect bond and specific hysteresis rules; experimental validation on physical specimens would strengthen the digital twin claim.
