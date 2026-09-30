import sys

from .client import SyncClient
from .config import load_config
from .logger import get_logger


logger = get_logger(__name__)


def main():
    try:
        config = load_config()
        client = SyncClient(config)

        logger.info(
            "Desktop Sync %s starting",
            config["application"]["version"],
        )

        if not config["sync"]["enabled"]:
            logger.info("Synchronization is disabled")
            return 0

        if client.synchronize():
            logger.info("Synchronization completed")
            return 0

        logger.error("Synchronization failed")
        return 1

    except Exception as exc:
        logger.error("Startup failed: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())