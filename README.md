# PySpark Development Container

This repository contains a development container configuration for Apache Spark 3.5.5 with Python support, including Jupyter Notebooks and debugging capabilities.

## Prerequisites

- Docker
- Visual Studio Code
- VS Code Dev Containers extension

## Getting Started

1. Clone this repository
2. Open the repository in VS Code
3. When prompted, click "Reopen in Container" or run the "Dev Containers: Reopen in Container" command from the Command Palette (Ctrl/Cmd + Shift + P)
4. Jupyter Notebook will automatically start and be available at http://localhost:8888

## Features

- Apache Spark 3.5.5
- Python 3 support
- Jupyter Notebooks (auto-starting)
- Debugging support with debugpy
- Azure Storage integration

## Using Jupyter Notebooks

### Quick Start
The simplest way to start Jupyter (the script is pre-installed in the workspace):

1. Open a terminal in VS Code (Terminal → New Terminal)
2. Run:
   ```bash
   ./start-jupyter.sh
   ```
3. Open your browser to http://localhost:8888

### Manual Start
If needed, you can also start Jupyter directly with:
```bash
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''
```

Note: For security in development environments, authentication is disabled by default. Do not use this configuration in production.

### Verifying Jupyter is Running
To check if Jupyter is already running:
1. Open a terminal and run:
   ```bash
   ps aux | grep jupyter
   ```
2. If no Jupyter process is found, follow the startup steps above
3. If a process is found but you can't access the notebook, check the Ports panel in VS Code to ensure port 8888 is forwarded

## Debugging Python Scripts

### Setting Up for Debugging

1. Make sure you're inside the dev container (you should see "Dev Container: Spark Dev Container" in the bottom-left corner of VS Code)
2. Your Python script should include the debugpy setup code at the top:
   ```python
   import debugpy
   debugpy.listen(("0.0.0.0", 5678))
   print("Waiting for debugger attach...")
   debugpy.wait_for_client()
   ```

### Starting a Debug Session

1. Set breakpoints in your code by clicking in the left margin (gutter) next to the line numbers where you want to pause execution
2. Open a terminal in VS Code (Terminal → New Terminal)
3. Run your Python script:
   ```bash
   python3 your_script.py
   ```
4. The script will start and show "Waiting for debugger attach..."
5. You should see a notification: "Your application running on port 5678 is available"
6. Go to the Run and Debug view in VS Code (Ctrl/Cmd + Shift + D)
7. Select "Python: Remote Attach" from the dropdown at the top
8. Click the green play button or press F5 to attach the debugger

### Using the Debugger

Once the debugger is attached, you can:
- Use F5 to continue execution
- Use F10 to step over lines
- Use F11 to step into functions
- Use Shift + F11 to step out of functions
- Use the Variables panel to inspect variable values
- Use the Debug Console to execute Python commands in the current context
- Use the Call Stack to understand where you are in the code
- Use the Watch panel to monitor specific expressions

### Debugging Tips

1. If you get "Address already in use" error:
   - This means a previous debug session is still running
   - Find the process: `ps aux | grep python`
   - Kill the old process: `kill <process_id>`

2. If the debugger won't connect:
   - Make sure you're running the script first, then attaching the debugger
   - Check that port 5678 is properly forwarded (you should see it in the Ports panel)
   - Try restarting VS Code or rebuilding the container

3. Common Breakpoint Locations:
   - Before and after DataFrame transformations
   - Before showing or writing data
   - Inside complex data processing functions
   - Before API calls or external system interactions

## Azure Storage Integration

To use Azure Storage:

1. Open `sample_spark.py`
2. Replace the placeholder values:
   - YOUR_STORAGE_ACCOUNT
   - YOUR_CONTAINER
   - YOUR_STORAGE_KEY
3. Run the script with debugging enabled

## Container Configuration

- The dev container is configured in `.devcontainer/devcontainer.json`
- Dockerfile is located in `.devcontainer/Dockerfile`
- Debugging configuration is in `.vscode/launch.json` 