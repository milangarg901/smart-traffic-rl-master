# 🚦 Smart Traffic RL — User Manual & Setup Guide

Multi-Agent Reinforcement Learning for Intelligent Traffic Control.

---

## 📋 Prerequisites & System Requirements

Before running the project, ensure you have the following installed:

| Requirement | Supported Versions | Purpose |
| :--- | :--- | :--- |
| **Python** | 3.10, 3.11, or 3.14+ | Core runtime environment |
| **SUMO Simulator** | 1.19+ (recommended 1.26+) | Microscopic traffic simulation engine |
| **pip** | Latest | Python package manager |
| **PowerShell / Terminal** | 5.1+ (Windows) / Bash (Linux/macOS) | CLI Execution |

---

## ⚙️ Environment Setup

### 1. SUMO Simulator Installation
The simulator **SUMO** (Simulation of Urban MObility) must be installed on your system.

*   **Windows (via winget - Recommended)**:
    ```powershell
    winget install EclipseFoundation.SUMO --silent
    ```
*   **Windows (Manual)**: Download the installer from the [Eclipse SUMO website](https://sumo.dlr.de/docs/Downloads.php).
*   **Linux (Ubuntu/Debian)**:
    ```bash
    sudo add-apt-repository ppa:sumo/stable
    sudo apt-get update && sudo apt-get install sumo sumo-tools
    ```
*   **macOS (via Homebrew)**:
    ```bash
    brew install sumo
    ```

### 2. Configure environment variables
Ensure `SUMO_HOME` points to your SUMO installation folder:
*   **Windows**:
    ```powershell
    [System.Environment]::SetEnvironmentVariable("SUMO_HOME", "C:\Program Files (x86)\Eclipse\Sumo", "User")
    ```
*   **Linux/macOS**: Add this to your `.bashrc` or `.zshrc`:
    ```bash
    export SUMO_HOME="/usr/share/sumo"  # or homebrew path on macOS
    ```

---

## 🚀 Running the Project

### Step 1: Create & Activate Virtual Environment
```powershell
# Create venv
python -m venv venv

# Activate on Windows
.\venv\Scripts\Activate.ps1

# Activate on Linux/macOS
source venv/bin/activate
```

### Step 2: Install Packages
```bash
pip install -r requirements.txt
```

### Step 3: Launch Interactive CLI Menu
```bash
python main.py
```

The terminal will present the interactive main menu:
```text
┌─────────────────────────────────────────────────────────────┐
│                       MAIN MENU                             │
├─────────────────────────────────────────────────────────────┤
│  1. Train Single Agent (PPO with Curriculum Learning)       │
│  2. Train Multi-Agent (MAPPO for 9 Intersections)           │
│  3. Run Dashboard (Real-time Visualization)                 │
│  4. Run Evaluation Only                                     │
│  5. Run Adversarial Tests                                   │
│  6. Generate SUMO Network                                   │
│  7. Run All Tests                                           │
│  8. Exit                                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧭 Recommended Execution Order (First-Time Run)

1.  **Generate SUMO Network (Option 6)**: Builds the custom 3x3 intersection city grid files.
2.  **Run All Tests (Option 7)**: Verifies your environment, SUMO integration, and environment observation spaces are fully operational.
3.  **Run Dashboard (Option 3)**: Launches the interactive dashboard to visualize current performance and real-time inference on the pre-trained weights.
4.  **Train Single Agent (Option 1)**: Initiates curriculum learning on the center intersection.
5.  **Train Multi-Agent (Option 2)**: Fine-tunes weights across all 9 intersections cooperatively.

---

## 📊 Direct Command-Line Access
You can bypass the menu interface by launching main.py directly with flags:

```bash
# Run training pipelines
python main.py --mode train      # Curriculum training
python main.py --mode multi      # Multi-agent fine-tuning

# Visualizations & Audits
python main.py --mode dashboard  # Live Streamlit dashboard
python main.py --mode eval       # Baseline comparison
python main.py --mode test       # Execution test suites
```

---

## 🛠️ Troubleshooting

| Issue | Root Cause | Solution |
| :--- | :--- | :--- |
| `ModuleNotFoundError` | Virtual environment inactive | Activate the venv: `.\venv\Scripts\Activate.ps1` |
| `traci.exceptions.FatalTraCIError` | `SUMO_HOME` is not set | Set your `SUMO_HOME` environment variable |
| `Execution Policy Error` | Windows restriction on scripts | Run: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |
| Port Conflict (8501) | Dashboard is already running | Launch with custom port: `streamlit run dashboard/app.py --server.port 8502` |
