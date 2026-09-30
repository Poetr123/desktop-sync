import socket
import time

from .logger import get_logger


logger = get_logger(__name__)


class SyncClient:
    def __init__(self, config):
        self.config = config

        endpoint = config["endpoint"]
        sync = config["sync"]

        self.host = endpoint["host"]
        self.port = endpoint["port"]
        self.path = endpoint["path"]

        self.connect_timeout = sync["connect_timeout"]
        self.read_timeout = sync["read_timeout"]
        self.max_retries = sync["max_retries"]
        self.retry_delay = sync["retry_delay_seconds"]

    def collect_metadata(self):
        hostname = socket.gethostname()

        return {
            "client": self.config["application"]["name"],
            "version": self.config["application"]["version"],
            "hostname": hostname,
        }

    def build_payload(self):
        metadata = self.collect_metadata()

        body = (
            "client={client}\n"
            "version={version}\n"
        ).format(**metadata)

        return body.encode()

    def synchronize(self):
        payload = self.build_payload()

        for attempt in range(1, self.max_retries + 1):
            try:
                return self._send(payload)

            except (OSError, TimeoutError) as exc:
                logger.warning(
                    "Synchronization attempt %d failed: %s",
                    attempt,
                    exc,
                )

                if attempt < self.max_retries:
                    time.sleep(self.retry_delay)

        return False

    def _send(self, payload):
        logger.info(
            "Synchronizing with %s:%s",
            self.host,
            self.port,
        )

        with socket.create_connection(
            (self.host, self.port),
            timeout=self.connect_timeout,
        ) as sock:

            sock.settimeout(self.read_timeout)

            request = (
                f"POST {self.path} HTTP/1.1\r\n"
                f"Host: {self.host}\r\n"
                "Content-Type: application/octet-stream\r\n"
                f"Content-Length: {len(payload)}\r\n"
                "Connection: close\r\n"
                "\r\n"
            ).encode() + payload

            sock.sendall(request)

            response = sock.recv(4096)

            return response.startswith(b"HTTP/1.1 200")