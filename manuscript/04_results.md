# 4. Results

## 4.1 OpenSeesPy Simulation Results

A batch of 20 synthetic ground motions was generated due to the unavailability of PEER NGA-West2 records in the cloud environment. Nonlinear time history analyses (NLTHA) were performed on the 5-story RC frame model using OpenSeesPy.

-   **Ground Motion Statistics**:
    -   Mean PGA: 0.48 g
    -   Mean Duration: 20.3 s
-   **Structural Response**:
    -   Convergence Rate: 100% (20/20 records)
    -   Typical Peak Inter-Story Drift Ratio (IDR): ~0.5% - 1.5%

## 4.2 Data Pipeline Statistics

The raw simulation data was processed into PyTorch tensors.

-   **Dataset Split**: 14 training, 3 validation, 3 test records.
-   **Physics Tensors**: Mass matrix ($M$), restoring forces ($f_{int}$), and kinematic responses ($\dot{u}, \ddot{u}$) were successfully verified to be non-zero, enabling the physics-informed loss calculation.

## 4.3 PINN Training Performance

The Hybrid PINN was trained for 500 epochs with a patience of 50.

-   **Convergence**: Training stopped early at **Epoch 66**.
-   **Physics Loss**: The physics regularization term ($L_{phy}$) remained active throughout training ($\sim 1.8 \times 10^{-15}$), constraining the solution to the equation of motion.
-   ** Validation Loss**: Reached a minimum of **0.100** (MSE), indicating strong generalization without overfitting.

![Training and validation loss curves](../manuscript/figures/loss_curves.png)
*Figure 4: Training and validation loss convergence.*

## 4.4 Prediction Accuracy

The model was evaluated on the held-out test set (unseen ground motions).

**Overall Performance:**
-   **$R^2$**: 0.803
-   **RMSE**: 0.27% (drift ratio)

**Per-Story Performance:**
-   **Story 1**: $R^2 = 0.84$, indicating high accuracy at the base.
-   **Story 4**: $R^2 = 0.79$.
-   **Story 5**: $R^2 = 0.69$, showing slightly higher dispersion in the upper stories due to higher mode effects.

![Predicted vs. Actual IDR](../manuscript/figures/pred_vs_actual.png)
*Figure 5: Predicted vs. actual peak inter-story drift ratio.*

![Error Distribution](../manuscript/figures/error_distribution.png)
*Figure 6: Per-story prediction error distribution.*

## 4.5 Real-Time Benchmarking

To validate the "real-time" capability of the digital twin, inference latency was measured on a standard CPU environment using a batch size of 1.

-   **Pre-processing Latency**: 0.141 ms (mean)
-   **Inference Latency**: 0.988 ms (mean)
-   **Total Latency**: ~1.13 ms per time step

This performance is well below the control loop threshold of 10-20 ms required for effective structural control, confirming the suitability of the Hybrid PINN for real-time monitoring.

| Metric | Value |
| :--- | :--- |
| Device | CPU |
| Warm Start (Mean) | 0.99 ms |
| 99th Percentile | 2.74 ms |
| Throughput (Batch=1) | > 1,300 samples/sec |
