# Deployment

## Requirements

The client requires:

- Python 3.10 or newer
- POSIX-compatible shell
- Network connectivity to the synchronization service

## Installation

Run:

    ./scripts/install.sh

The installer prepares the runtime directories and performs a basic
configuration validation.

## Manual Installation

The client may also be started directly from the repository:

    python3 -m src.main

## Service Integration

The client can be launched by an external process manager.

The application itself does not install or modify system services.

## Configuration

Before deployment, review:

    config/default.json

The following values are particularly relevant:

- sync interval
- connection timeout
- read timeout
- maximum retries
- synchronization endpoint

## Health Check

After deployment, run:

    ./scripts/healthcheck.sh

A successful check prints the current client version and configuration
status.

## Rollback

To roll back to an earlier release, check out the corresponding Git tag
or commit and restart the client.