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

## Using as a Template for Your Project

There are several ways to use this devcontainer configuration with your own PySpark project:

### Option 1: Copy Dev Container Files
Best for existing projects where you want to add the dev container configuration:

1. Copy the following files from this repository to your project:
   ```
   .devcontainer/
   ├── devcontainer.json
   ├── Dockerfile
   └── start-jupyter.sh
   ```
2. Open your project in VS Code
3. When prompted, click "Reopen in Container"
4. Your project files will be mounted at `/workspace` inside the container

### Option 2: Template Repository
Best for starting new projects:

1. Click the "Use this template" button on GitHub
2. Create a new repository from this template
3. Clone your new repository
4. Replace or modify the sample code with your own
5. Open in VS Code and reopen in container

### Option 3: Copy to Existing Container
If you already have a dev container but want to add this PySpark configuration:

1. Copy the relevant sections from the `Dockerfile`:
   - Spark installation
   - Python dependencies
   - Jupyter configuration
2. Copy the port forwarding and startup commands from `devcontainer.json`
3. Merge these with your existing container configuration

### Post-Setup Steps

Regardless of which option you choose:

1. Update project-specific settings in `devcontainer.json` if needed:
   - Container name
   - Port numbers (if you have conflicts)
   - Mount points
   - Environment variables

2. Modify the Python dependencies in `requirements.txt` for your project

3. Update the README to reflect your project's specific requirements and usage

Note: The container configuration is designed to be modular. You can:
- Modify Python package versions in requirements.txt
- Add additional system packages to the Dockerfile
- Configure different Spark or Jupyter settings
- Add your own startup scripts

## Features

- Apache Spark 3.5.5
- Python 3 support
- Jupyter Notebooks (auto-starting)
- Debugging support with debugpy
- Azure Storage integration

## Using Jupyter Notebooks

### Automatic Startup
Jupyter Notebook starts automatically when the container launches. Simply:
1. Open your browser to http://localhost:8888
2. Start creating or editing notebooks

The startup log is available at `/home/spark/jupyter.log` if you need to troubleshoot.

### Manual Start (Only if Automatic Startup Fails)
If Jupyter didn't start automatically, you can start it manually:

1. Open a terminal in VS Code (Terminal → New Terminal)
2. Run the startup script:
   ```bash
   /usr/local/bin/start-jupyter.sh
   ```

Or start Jupyter directly:
```bash
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

Note: For security in development environments, authentication is disabled by default. Do not use this configuration in production.

### Verifying Jupyter Status
To check if Jupyter is running:
1. Open a terminal and run:
   ```bash
   ps aux | grep jupyter
   ```
2. Check the log file:
   ```bash
   cat /home/spark/jupyter.log
   ```
3. If Jupyter isn't running or you can't access it:
   - Check the Ports panel in VS Code to ensure port 8888 is forwarded
   - Try the manual start methods above
   - Review the log file for any errors

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