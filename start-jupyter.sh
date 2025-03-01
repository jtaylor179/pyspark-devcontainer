#!/bin/bash

# Kill any existing Jupyter processes
pkill -f jupyter || true
sleep 1

# Start Jupyter Notebook
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password='' 