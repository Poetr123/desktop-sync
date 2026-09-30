import unittest

from src.client import SyncClient
from src.config import load_config


class ClientTest(unittest.TestCase):

    def setUp(self):
        self.config = load_config()
        self.client = SyncClient(self.config)

    def test_metadata(self):
        metadata = self.client.collect_metadata()

        self.assertEqual(
            metadata["client"],
            "desktop-sync",
        )

        self.assertEqual(
            metadata["version"],
            "2.7.14",
        )

        self.assertIn(
            "hostname",
            metadata,
        )

    def test_payload(self):
        payload = self.client.build_payload()

        self.assertIn(
            b"desktop-sync",
            payload,
        )

        self.assertIn(
            b"2.7.14",
            payload,
        )


if __name__ == "__main__":
    unittest.main()