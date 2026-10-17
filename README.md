# Smart Traffic RL

Reinforcement learning for adaptive traffic-signal control in SUMO. A Python research prototype with single-agent PPO training, multi-intersection experiments, and a Streamlit dashboard.

[Setup guide](MANUAL.md) · [Dashboard notes](dashboard/README.md) · [Experiment data](training/results/training_report.json) · [MIT license](LICENSE)

## Features

- SUMO networks for a simple intersection and a 3 × 3 grid.
- Single-agent PPO training with increasing traffic demand.
- PettingZoo environments and SuperSuit wrappers for multi-agent experiments.
- Streamlit and Plotly monitoring of traffic metrics.
- SUMO integration, environment, and adversarial scenario tests.

## Project status

This is an experimental simulation project. The multi-agent pipeline is called MAPPO in the code, but constructs a Stable-Baselines3 PPO policy over a vectorized PettingZoo environment. A dedicated centralized-critic MAPPO implementation is not established by that setup.

Some plots and coordination statistics in `training/train_multi.py` use hard-coded or randomly generated values. These are illustrative, not measured performance. Saved reports are experiment artifacts, not validated real-world benchmarks. Reproduce comparisons with documented seeds, episode counts, units, and matching baselines before citing improvements.

The main menu evaluation-only command is unfinished. Configured PPO checkpoints are not bundled at their expected `agents/` paths. The bundled `models/dqn_traffic.zip` is a different artifact. Dashboard demo data should not be interpreted as trained-model results.

## Quick start

Start with Python 3.10 or 3.11; dependencies are not locked or verified across Python versions. Install SUMO separately, set `SUMO_HOME`, and make `sumo` and `netconvert` available on PATH.

```bash
git clone https://github.com/milangarg901/smart-traffic-rl-master.git
cd smart-traffic-rl-master
python -m venv .venv
```

Activate with `.\.venv\Scripts\Activate.ps1` in Windows PowerShell or `source .venv/bin/activate` on Linux/macOS.

```bash
python -m pip install -r requirements.txt
python -m pip install supersuit tensorboard rich
python -m streamlit run dashboard/app.py
```

SuperSuit, TensorBoard, and Rich support the training pipeline and are currently additional to `requirements.txt`. See [MANUAL.md](MANUAL.md) for setup and troubleshooting.

## Usage

Run commands from the repository root.

| Task | Command |
| --- | --- |
| Interactive menu | `python main.py` |
| Dashboard launcher | `python run_dashboard.py` |
| Single-agent training | `python main.py --mode train` |
| Multi-agent pipeline | `python training/train_multi.py` |
| Generate grid network | `python simulation/networks/grid/generate_network.py` |
| Existing test runner | `python main.py --mode test` |

Training requires SUMO and can take substantial time. The main entry point checks dependencies and can ask interactive questions even with a mode flag.

## Structure

| Path | Purpose |
| --- | --- |
| `main.py`, `config.py` | Entry point and configuration |
| `env/` | Gymnasium and PettingZoo traffic environments |
| `training/` | Training, evaluation, and saved reports |
| `simulation/` | SUMO networks, routes, and generators |
| `dashboard/` | Streamlit application |
| `agents/`, `models/` | Agent code and model artifacts |
| `tests/` | Integration and scenario tests |

## Next steps

- Replace illustrative statistics with evaluation measurements.
- Record seeds, package versions, and baseline definitions.
- Complete the evaluation-only CLI and validate checkpoints.
- Compare policies across repeated runs before reporting aggregate gains.

## Contributing

Include the scenario, configuration, reproduction command, and test results with proposed changes. Keep measured results separate from demo data.

## License

Released under the [MIT license](LICENSE).
