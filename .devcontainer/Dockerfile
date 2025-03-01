# Use the Apache Spark 3.5.5 base image with Scala 2.12, Java 11, and Python 3 on Ubuntu
FROM apache/spark:3.5.5-scala2.12-java11-python3-ubuntu

# Switch to root user to install additional packages
USER root

# Ensure system is up to date and install necessary packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    curl \
    sudo \
    bash \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

# Copy and setup startup script
COPY start-jupyter.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start-jupyter.sh && \
    chown spark:spark /usr/local/bin/start-jupyter.sh

# Configure sudo for spark user
RUN echo "spark ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/spark && \
    chmod 0440 /etc/sudoers.d/spark

# Create all necessary directories and set permissions
RUN mkdir -p \
    # Home directory structure
    /home/spark \
    /home/spark/.local/{bin,lib,share} \
    /home/spark/.jupyter \
    /home/spark/.spark \
    /home/spark/spark-events \
    /home/spark/.ssh \
    /home/spark/tmp \
    /home/spark/.cache/pip \
    # VS Code/Cursor directories
    /home/spark/.cursor-server/{bin,data/Machine,extensions} \
    /home/spark/.vscode-remote \
    /vscode/{extensions,data} \
    # Workspace structure
    /workspace/.{jupyter,ipython,local} \
    /workspace/{notebooks,data} \
    # Spark logs
    ${SPARK_HOME}/logs \
    && \
    # Set up spark user
    usermod -s /bin/bash spark && \
    usermod -aG sudo spark && \
    # Set ownership
    chown -R spark:spark /home/spark /vscode /workspace ${SPARK_HOME}/logs && \
    # Set permissions
    chmod -R 755 /home/spark /vscode /workspace ${SPARK_HOME}/logs && \
    chmod 700 /home/spark/.ssh

# Set environment variables
ENV HOME=/home/spark \
    PYTHONUSERBASE=/home/spark/.local \
    PATH=/home/spark/.local/bin:$PATH \
    PYTHONPATH=/opt/spark/python:/opt/spark/python/lib/py4j-0.10.9.7-src.zip:/opt/spark/python/lib/pyspark.zip:/workspace \
    SPARK_HOME=/opt/spark \
    SPARK_CONF_DIR=/home/spark/.spark \
    SPARK_LOG_DIR=/home/spark/spark-events \
    TMPDIR=/home/spark/tmp \
    JAVA_TOOL_OPTIONS="-Djava.io.tmpdir=/home/spark/tmp" \
    JUPYTER_CONFIG_DIR=/home/spark/.jupyter

# Switch to spark user for remaining operations
USER spark

# Install Python packages as spark user
RUN pip3 install --user --no-cache-dir jupyter debugpy azure-storage-blob

# Configure Jupyter with heredoc for better readability
RUN echo 'c.NotebookApp.ip = "0.0.0.0"' > /home/spark/.jupyter/jupyter_notebook_config.py && \
    echo 'c.NotebookApp.allow_root = True' >> /home/spark/.jupyter/jupyter_notebook_config.py && \
    echo 'c.NotebookApp.open_browser = False' >> /home/spark/.jupyter/jupyter_notebook_config.py && \
    echo 'c.NotebookApp.token = ""' >> /home/spark/.jupyter/jupyter_notebook_config.py && \
    echo 'c.NotebookApp.password = ""' >> /home/spark/.jupyter/jupyter_notebook_config.py && \
    echo 'c.NotebookApp.notebook_dir = "/workspace"' >> /home/spark/.jupyter/jupyter_notebook_config.py

# Set up shell configuration files with minimal exports (avoid duplicating ENV)
RUN touch /home/spark/.bashrc /home/spark/.bash_profile /home/spark/.profile && \
    echo 'if [ -f ~/.bashrc ]; then . ~/.bashrc; fi' > /home/spark/.bash_profile && \
    # Only add PATH modifications and any variables that need to be available in interactive shells
    echo 'export PATH=/home/spark/.local/bin:$PATH' >> /home/spark/.bashrc

# Set the working directory
WORKDIR /workspace

# Expose necessary ports
EXPOSE 8888 5678 