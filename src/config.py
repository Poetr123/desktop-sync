import json
import os


DEFAULT_CONFIG = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "config",
    "default.json",
)


def load_config(path=DEFAULT_CONFIG):
    with open(path, "r", encoding="utf-8") as file:
        config = json.load(file)

    validate_config(config)

    return config


def validate_config(config):
    required_sections = [
        "application",
        "sync",
        "endpoint",
        "runtime",
    ]

    for section in required_sections:
        if section not in config:
            raise ValueError(
                f"Missing configuration section: {section}"
            )

    endpoint = config["endpoint"]

    if not endpoint.get("host"):
        raise ValueError("Endpoint host is empty")

    if not endpoint.get("port"):
        raise ValueError("Endpoint port is missing")

    if not isinstance(endpoint["port"], int):
        raise ValueError("Endpoint port must be an integer")

    application = config["application"]

    if not application.get("environment"):
        raise ValueError("Application environment is missing")

    sync = config["sync"]

    if sync.get("interval_seconds", 0) <= 0:
        raise ValueError("Invalid synchronization interval")