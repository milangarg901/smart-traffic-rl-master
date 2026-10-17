#!/usr/bin/env python3
"""Launch the dashboard using the active Python environment."""
import importlib.util
from pathlib import Path
import subprocess
import sys


def main():
    if importlib.util.find_spec("streamlit") is None:
        print("Streamlit is missing. Install dependencies with:")
        print(f'"{sys.executable}" -m pip install -r requirements.txt')
        return 1

    from config import dashboard_config, paths_config

    project_root = Path(__file__).resolve().parent
    model_path = Path(paths_config.MULTI_AGENT_MODEL)
    if not model_path.is_absolute():
        model_path = project_root / model_path
    if not model_path.exists():
        print(f"Warning: configured multi-agent model not found at {model_path}")
        print("Demo data must not be interpreted as trained-model results.")

    print(
        f"Dashboard: http://{dashboard_config.DEFAULT_HOST}:"
        f"{dashboard_config.DEFAULT_PORT}"
    )
    try:
        result = subprocess.run(
            [
                sys.executable, "-m", "streamlit", "run",
                str(project_root / "dashboard" / "app.py"),
                "--server.port", str(dashboard_config.DEFAULT_PORT),
                "--server.address", dashboard_config.DEFAULT_HOST,
            ],
            cwd=str(project_root),
        )
        return result.returncode
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
