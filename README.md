# Desktop Sync

Desktop Sync is a lightweight client used to synchronize workstation
metadata and application state with the internal synchronization service.

## Requirements

- Python 3.10+
- Linux or macOS
- Network access to the configured synchronization endpoint

## Installation

Clone the repository and run:

    ./scripts/install.sh

The installer creates the required runtime directories and prepares
the local configuration.

## Configuration

The default configuration is located at:

    config/default.json

Logging configuration is located at:

    config/logging.json

Environment variables may be used to override selected configuration
values.

## Running

Start the client with:

    python3 -m src.main

For a health check:

    ./scripts/healthcheck.sh

## Project Layout

    config/     Runtime configuration
    docs/       Project documentation
    scripts/    Utility scripts
    src/        Application source
    tests/      Automated tests

## Development

Run the test suite with:

    python3 -m unittest discover -s tests

## Release Notes

See CHANGELOG.md for release history.