# Docker Container Manager

A simple Python-based Docker Container Manager to list, start, and stop Docker containers interactively via the command line.

## Features

- **List All Containers:** View all Docker containers, including stopped and running ones.
- **Start a Stopped Container:** Restart any stopped container using its ID.
- **Stop a Running Container:** Stop any running container using its ID.
- **Exit Option:** Easily exit the manager with a menu option.

## Requirements

- Python 3.x
- Docker installed and running on your machine
- Virtual environment
- `docker` Python package (`pip install docker`)

## Usage

1. Clone the repository.
2. Ensure Docker is running on your machine.
3. Run the script:

    ```bash
    python main.py
