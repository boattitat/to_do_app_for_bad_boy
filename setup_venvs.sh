#!/bin/bash

# Function to setup venv and install requirements
setup_venv() {
    local dir=$1
    echo "Setting up venv for $dir..."
    
    cd "src/$dir" || exit
    
    # Create venv if it doesn't exist
    if [ ! -d ".venv" ]; then
        python3.11 -m venv .venv
    fi
    
    # Activate venv and install requirements
    source .venv/bin/activate
    pip install -r requirements.txt
    deactivate
    
    cd ../..
}

# Setup venv for each project
setup_venv "duplicator"
setup_venv "finalizer"
setup_venv "session_manager"

echo "All virtual environments have been setup successfully!"
