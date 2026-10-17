# Smart Traffic RL — Setup and usage

## Environment

Start with Python 3.10 or 3.11. Dependencies are not locked, so other Python versions and package combinations require testing.

Install SUMO using the [official download instructions](https://sumo.dlr.de/docs/Downloads.php). Set `SUMO_HOME` to your installation directory and add its `bin` directory to PATH. Verify both `sumo --version` and `netconvert --version`. The Python TraCI package does not replace the external network-generation tools.

## Install dependencies

From the repository root:

```bash
python -m venv .venv
```

Activate with `.\.venv\Scripts\Activate.ps1` in Windows PowerShell, or `source .venv/bin/activate` on Linux/macOS. If activation is unavailable, invoke the environment Python directly.

```bash
python -m pip install -r requirements.txt
python -m pip install supersuit tensorboard rich
```

## Start the dashboard

```bash
python run_dashboard.py
```

The launcher uses the active Python interpreter, the repository directory, and the dashboard host/port in `config.py`. It reports missing Streamlit without automatically modifying the environment. Missing configured model weights produce a warning. Demo data is not evidence of trained-policy performance.

Alternatively:

```bash
python -m streamlit run dashboard/app.py
```

## Simulation and training

Run from the repository root:

```bash
# Generate grid network (requires netconvert)
python simulation/networks/grid/generate_network.py

# Open the interactive menu
python main.py

# Train single-agent PPO (asks for confirmation)
python main.py --mode train

# Multi-agent training and evaluation pipeline
python training/train_multi.py

# Run existing test suites
python main.py --mode test
```

Review traffic demand, reward weights, training budgets, and checkpoint paths in `config.py` before a long run. Configured PPO checkpoints are `agents/ppo_final.zip` and `agents/mappo_final.zip`; the bundled `models/dqn_traffic.zip` is a different artifact. Check algorithm and observation/action compatibility before reusing weights.

## Evaluation limitations

The main menu evaluation-only mode is unfinished. The multi-agent script has a `--skip-training` option for a compatible checkpoint, but evaluation still needs validation. Some plots and coordination statistics contain illustrative constants or random data. Do not report these as measured gains.

For reproducible experiments, save the commit, dependency versions, SUMO version, seeds, scenario, checkpoint, episode count, baseline definition, metric units, and raw per-episode measurements.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Missing Python module | Use `python -m pip` with the interpreter running the app. |
| Missing SuperSuit | Install `supersuit` in the active environment. |
| SUMO or netconvert not found | Check installation, PATH, and `SUMO_HOME`. |
| TraCI failure | Inspect SUMO error output, network paths, and port availability. |
| Dashboard port occupied | Run `python -m streamlit run dashboard/app.py --server.port 8502`. |
| PPO checkpoint missing | Train the corresponding pipeline and verify configured paths. |
| Package installation fails | Check support for your Python and platform; do not assume a dependency-free install is complete. |

See the [project overview](README.md) for features and current status.
