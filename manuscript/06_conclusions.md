# 6. Conclusions

## 6.1 Key Findings

This study developed and validated a Hybrid Digital Twin framework for seismic response prediction of reinforced concrete buildings, demonstrating its viability with both synthetic and real earthquake data. The key findings are:

1.  **Physics-Informed Accuracy**: The PINN model achieved $R^2 = 0.791$ on synthetic data and $R^2 = 0.650$ on real PEER NGA-West2 records, with RMSE values of 0.26% and 0.76% drift ratio, respectively. The physics loss term ($L_{phy}$) remained active throughout training, constraining outputs to satisfy the equation of motion $M\ddot{u} + C\dot{u} + f_{int}(u) = -M \cdot \mathbf{1} \cdot \ddot{u}_g$.
2.  **Real-Time Capability**: With an average total latency of **~1.13 ms** per time step on a standard CPU, the framework operates well within the 10–20 ms threshold required for real-time structural health monitoring and control.
3.  **Data Efficiency**: The hybrid loss function enabled effective learning from only **21 ground motion records** (342 augmented samples), a significant advantage over purely data-driven approaches that typically require thousands of simulations.
4.  **Parametric Flexibility**: The $N$-story architecture allows dynamic configuration of building height (tested at $N=3$, scalable to $N=8$), enabling rapid deployment for different building typologies.

## 6.2 Contributions

-   **Open-Source Pipeline**: A fully reproducible, end-to-end Python pipeline integrating OpenSeesPy simulation with PyTorch-based PINN training, parameterized for $N$-story buildings.
-   **Real Data Validation**: First demonstration of a physics-informed seismic surrogate model validated against PEER NGA-West2 records (Friuli, Imperial Valley events).
-   **Hybrid Loss Formulation**: Implementation of the multi-degree-of-freedom equation of motion as a differentiable loss function for arbitrary $N$-story shear building models.
-   **Cloud-Ready Architecture**: Containerized (Docker/Codespaces) and optimized for deployment.

## 6.3 Future Work

1.  **Full PEER Campaign**: Complete the 100-record simulation campaign to achieve the target $R^2 \geq 0.75$.
2.  **Variable Cross-Sections**: Implement story-dependent column sizing for buildings taller than 8 stories.
3.  **3D Extensions**: Extend the physics formulation to capture torsional and bidirectional seismic effects.
4.  **Experimental Validation**: Calibrate the digital twin against shake table test data.
5.  **Edge Deployment**: Deploy the quantized model on embedded hardware (Jetson Nano, Raspberry Pi) for decentralized SHM.
