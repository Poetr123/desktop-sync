# Architecture

## Overview

Desktop Sync consists of a small local client responsible for collecting
runtime information and sending synchronization records to a remote
service.

The client is intentionally lightweight and does not maintain a persistent
database.

## Components

### Client

The client coordinates the synchronization process.

Responsibilities:

- Load configuration.
- Collect local metadata.
- Build synchronization records.
- Send records to the configured endpoint.
- Handle retries.
- Record synchronization state.

### Configuration

Configuration is loaded from `config/default.json`.

Runtime configuration may be overridden by environment variables.

### Logger

Application logging is handled through the standard Python logging
framework.

## Synchronization Flow

The normal synchronization flow is:

1. Load configuration.
2. Validate configuration.
3. Collect client metadata.
4. Build synchronization payload.
5. Connect to the synchronization endpoint.
6. Submit the payload.
7. Process the response.
8. Update local synchronization state.

## Failure Handling

Transient connection errors are retried according to the configured
retry policy.

A synchronization attempt is considered successful only after the
remote endpoint acknowledges the request.

## Runtime State

The client stores a small amount of runtime state under the configured
runtime directory.

Runtime state should not be committed to the repository.
## Runtime Directory Management

Temporary synchronization data is stored outside the source tree.
The cleanup utility can be used to remove stale runtime files without
affecting application configuration or source code.
