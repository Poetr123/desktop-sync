# Changelog

All notable changes to this project are documented in this file.

## [2.7.14] - 2026-09-21

### Changed

- Updated synchronization client.
- Improved retry handling.
- Reduced unnecessary connection attempts.
- Updated runtime logging.
- Refreshed deployment documentation.

### Fixed

- Fixed stale cache cleanup.
- Fixed malformed configuration handling.
- Fixed retry counter not being reset after successful synchronization.

## [2.7.13] - 2026-09-14

### Added

- Added connection health checks.
- Added configurable retry delay.
- Added additional client metadata.

### Fixed

- Fixed startup failure when runtime directory was missing.

## [2.7.12] - 2026-09-03

### Changed

- Refactored configuration loading.
- Improved error messages.
- Updated default logging format.

## [2.7.11] - 2026-08-26

### Fixed

- Fixed timeout handling during synchronization.
- Fixed an issue where interrupted synchronization left stale
  temporary files.

## [2.7.10] - 2026-08-12

### Added

- Initial stable release of the current synchronization workflow.