# Troubleshooting

## Client Does Not Start

Verify that Python is available:

    python3 --version

Then run:

    python3 -m src.main

directly to inspect startup errors.

## Configuration Error

Verify that:

    config/default.json

contains valid JSON.

The configuration loader reports the affected field when validation
fails.

## Synchronization Timeout

Check network connectivity and confirm that the configured endpoint is
reachable.

Review the connection and read timeout values in:

    config/default.json

## Repeated Retries

Repeated retries usually indicate one of the following:

- Remote endpoint unavailable.
- Network interruption.
- Invalid endpoint configuration.
- Remote service rejecting the request.

## Runtime Directory Problems

Remove stale runtime files and recreate the runtime directory:

    ./scripts/cleanup.sh

Then restart the client.

## Logging

The default logging configuration writes messages to standard output.

For additional information, run the client directly instead of using
the service manager.
## Host Metadata

The synchronization payload includes the local hostname for identifying
the originating workstation. The value is collected at runtime and is
not stored in the repository configuration.
