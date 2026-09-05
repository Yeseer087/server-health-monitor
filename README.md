# Server Health Monitor

A beginner-friendly Python server health monitoring application built with Docker and automated with GitHub Actions.

## Features

- Monitors CPU usage
- Monitors memory usage
- Monitors disk usage
- Monitors network usage
- Classifies resources as NORMAL, WARNING, or CRITICAL
- Records health reports in log files
- Runs inside a Docker container
- Includes a Docker health check
- Uses automated Python tests with pytest
- Uses Github Actions for CI

## Health Thresholds

| Usage | Status |
|---|---|
| 0% - 69% | NORMAL |
| 70% - 89% | WARNING |
| 90% - 100% | CRITICAL |

## Technologies

- Python
- Linux
- Docker
- Git % GitHub
- GitHub Actions
- pytest

## How It Works

The application continually checks CPU, memory, disk, and network information from the system.

It assign a status to CPU, memory, and disk based on their usage. The highest severity becomes the overall server status.

The results are displayed in the terminal and saved to 'logs/server.log'.

## Running Locally

Install the dependencies:

'''bash
pip3 install -r requirements.txt

