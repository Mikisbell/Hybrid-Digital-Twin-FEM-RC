# Hybrid Digital Twin for Seismic RC Buildings

Hybrid Digital Twin framework for real-time seismic damage prediction in RC buildings using OpenSeesPy and Physics-Informed Machine Learning (PIML). Developed for Engineering 4.0 research.

**Target Journal**: [Civil Engineering and Architecture — HRPUB](http://www.hrpub.org/journals/jour_info.php?id=48)

## Overview

This framework combines:
- **OpenSeesPy** [1]: Non-linear time history analysis (NLTHA) of 5-story RC frames per ACI 318-19 [5]
- **Physics-Informed Neural Networks (PINNs)** [3]: Real-time structural damage prediction with physics constraints
- **Digital Twin Technology** [4]: Synchronized physical-digital representation for resilience assessment

The system predicts inter-story drifts in real-time (≤ 100 ms inference), enabling proactive structural health monitoring and seismic risk assessment.

### Physics-Informed Loss Function

The PINN embeds the equation of motion as a regularization term in the loss:

$$\mathcal{L}_{total} = \mathcal{L}_{data} + \lambda \left\| M\ddot{u} + C\dot{u} + Ku + M\iota\ddot{u}_g \right\|^2$$

Where the second term is the physics residual of the multi-degree-of-freedom system:
- $M$, $C$, $K$ — mass, damping, and stiffness matrices
- $\ddot{u}_g$ — ground acceleration input
- $\lambda$ — physics regularization weight (tunable hyperparameter)

## Project Structure

```
Hybrid-Digital-Twin-Seismic-RC/
├── src/                        # Source code
│   ├── opensees_analysis/      # OpenSeesPy RC model & NLTHA runners
│   ├── pinn/                   # Physics-Informed Neural Network
│   │   └── benchmark_latency.py  # Real-time latency validation (≤100 ms)
│   ├── preprocessing/          # Data pipeline & feature engineering
│   └── utils/                  # Notion sync, figure manager, helpers
├── data/                       # Data storage (heavy files git-ignored)
│   ├── raw/                    # Raw NLTHA simulation output
│   ├── processed/              # ML-ready datasets
│   ├── external/               # PEER NGA-West2 ground motions [2]
│   └── models/                 # Trained checkpoints & benchmarks
├── manuscript/                 # HRPUB paper (English only)
│   ├── 01_introduction.md      # Background & literature gap
│   ├── 02_objectives.md        # Research objectives
│   ├── 03_methods.md           # NLTHA + PINN + DT methodology
│   ├── 04_results.md           # Simulation & prediction results
│   ├── 05_discussion.md        # Interpretation & comparison
│   ├── 06_conclusions.md       # Findings & future work
│   ├── references.bib          # BibTeX (numeric correlative [1]–[N])
│   ├── figures/                # ≥300 DPI publication figures
│   └── tables/                 # Formatted data tables
├── notebooks/                  # Jupyter notebooks (EDA, training, demos)
├── .github/workflows/          # CI/CD & Notion sync automation
└── requirements.txt            # Python dependencies
```

> **Note**: Heavy data files (`.csv`, `.hdf5`, `.pkl`, model weights) are
> excluded via `.gitignore`. The data pipeline is fully reproducible from
> source code. See `data/README.md` for regeneration instructions.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mikisbell/Hybrid-Digital-Twin-Seismic-RC.git
cd Hybrid-Digital-Twin-Seismic-RC
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Getting Started

1. **Run OpenSeesPy Simulations**: Generate structural response data using non-linear time history analysis
2. **Process Data**: Prepare training datasets from simulation results
3. **Train PINN Models**: Develop physics-informed models for damage prediction
4. **Deploy Digital Twin**: Implement real-time prediction system

See individual directory READMEs for detailed information.

## Features

- Non-linear dynamic analysis of RC structures
- Physics-based neural network architectures
- Real-time inter-story drift prediction
- Seismic damage assessment
- Digital twin visualization and monitoring

## Requirements

- Python ≥3.10
- OpenSeesPy ≥3.5.0
- PyTorch ≥2.0.0
- NumPy, SciPy, Pandas
- Jupyter for notebooks
- notion-client (for automation sync)

## License

See [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## References

> **HRPUB citation format**: numeric correlative in brackets.

- [1] F. McKenna, "OpenSees: A Framework for Earthquake Engineering Simulation," *Comput. Sci. Eng.*, vol. 13, no. 4, pp. 58–66, 2011.
- [2] T. D. Ancheta *et al.*, "NGA-West2 Database," *Earthquake Spectra*, vol. 30, no. 3, pp. 989–1005, 2014.
- [3] M. Raissi, P. Perdikaris, and G. E. Karniadakis, "Physics-informed neural networks," *J. Comput. Phys.*, vol. 378, pp. 686–707, 2019.
- [4] F. Tao *et al.*, "Digital Twin in Industry: State-of-the-Art," *IEEE Trans. Ind. Inform.*, vol. 15, no. 4, pp. 2405–2415, 2019.
- [5] ACI Committee 318, *Building Code Requirements for Structural Concrete (ACI 318-19)*, ACI, 2019.
- [6] R. Zhang, Y. Liu, and H. Sun, "Physics-Informed Multi-LSTM Networks for Metamodeling of Nonlinear Structures," *CMAME*, vol. 369, 113226, 2020.
- [7] J. B. Mander, M. J. N. Priestley, and R. Park, "Theoretical Stress-Strain Model for Confined Concrete," *J. Struct. Eng.*, vol. 114, no. 8, pp. 1804–1826, 1988.
- [8] M. Menegotto and P. E. Pinto, "Method of Analysis for Cyclically Loaded RC Frames," *IABSE Symposium*, pp. 15–22, 1973.

## Citation

If you use this framework in your research, please cite:
```
[1] Mikisbell et al. (2026). "Hybrid Digital Twin for Real-Time Seismic
    Damage Prediction in RC Buildings Using Physics-Informed Neural Networks."
    Civil Engineering and Architecture, HRPUB. (Under review)
```
