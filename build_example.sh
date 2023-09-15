#!/bin/bash

# Install python3.8 and virtual environment
# sudo apt-get install python3.8 python3.8-venv

# Create a virtual environment
python3 -m venv pyvenv3

# Activate the virtual environment
source pyvenv3/bin/activate

# update pip
pip install --upgrade pip

# Install the pip package
pip install -r requirements.txt

# Compile the document
build-docs build

# Exit the virtual environment
deactivate