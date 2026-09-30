import unittest

from src.config import load_config


class ConfigTest(unittest.TestCase):

    def test_configuration_loads(self):
        config = load_config()

        self.assertIn("application", config)
        self.assertIn("sync", config)
        self.assertIn("endpoint", config)

    def test_application_version(self):
        config = load_config()

        self.assertEqual(
            config["application"]["version"],
            "2.7.14",
        )


if __name__ == "__main__":
    unittest.main()