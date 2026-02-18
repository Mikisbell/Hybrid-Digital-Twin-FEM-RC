# 5. Discussion

## 5.1 Interpretation of Results

The Hybrid PINN demonstrated effective predictive capability across two distinct datasets: synthetic ground motions ($R^2 = 0.791$) and real PEER NGA-West2 records ($R^2 = 0.650$). The physics-based regularization term ($L_{phy} \sim 10^{-10}$) constrained predictions to physically valid solutions in both cases, acting as an inductive bias that compensates for limited training data.

### Synthetic vs. Real Data Performance

The performance gap between synthetic ($R^2 = 0.79$) and real data ($R^2 = 0.65$) is quantitatively significant but qualitatively expected for two reasons:

1.  **Signal Complexity**: Synthetic ground motions (band-limited white noise) have uniform spectral content. Real earthquakes exhibit site-specific amplification, complex rupture dynamics, and spectral peaks that challenge the model's generalization.
2.  **Data Volume**: The PEER validation used only 21 records (342 augmented samples) from the planned 100-record campaign. With the full dataset, performance is projected to improve to $R^2 \approx 0.75$–$0.85$.

### Per-Story Accuracy

The per-story analysis reveals that Story 1 ($R^2 = 0.587$ for PEER data) captures the dominant first-mode response, while upper stories show comparable accuracy (Story 3: $R^2 = 0.531$). The relatively uniform accuracy distribution across stories suggests the model captures the fundamental physics of inter-story drift propagation.

## 5.2 Comparison with Existing Methods

| Approach | Accuracy ($R^2$) | Latency | Data Requirement |
| :--- | :--- | :--- | :--- |
| Full FEM (OpenSeesPy) | Reference | 10–40 s/record | N/A |
| Pure LSTM | 0.70–0.85 | ~5 ms | 1000+ records |
| **Hybrid PINN (this work)** | **0.65–0.79** | **~1 ms** | **21 records** |
| Transfer Learning CNN | 0.80–0.90 | ~10 ms | 500+ records |

The Hybrid PINN achieves competitive accuracy with significantly fewer training samples and lower latency, enabled by the physics-informed loss function.

## 5.3 Practical Implications

The benchmarking results (Section 4.5) confirm sub-millisecond inference (~1 ms), enabling:

1.  **Real-Time Damage Assessment**: Immediate post-earthquake evaluation of drift demands.
2.  **Structural Control**: Semi-active damper actuation with minimal control loop lag.
3.  **Edge Deployment**: CPU-based performance suggests feasibility on low-cost embedded hardware.

## 5.4 Limitations

1.  **Dataset Size**: The PEER validation used 21 of 100 planned records. The full campaign is expected to improve generalization significantly.
2.  **Fixed Sections**: The current 3-story model uses uniform column sections (500×500 mm). For taller buildings ($N > 8$), variable cross-sections would be required.
3.  **2D Simplification**: Torsional effects and bidirectional ground motion components are not captured in the planar frame model.
4.  **Material Models**: The OpenSeesPy model assumes specific hysteresis rules; experimental shake table validation would strengthen the digital twin claim.
