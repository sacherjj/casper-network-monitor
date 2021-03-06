import requests
from tempfile import TemporaryDirectory
import tarfile


PULL_URL = "http://genesis.casperlabs.io"
TEST_PULL_URL = "https://casper-genesis.make.services"
CONFIG_ARCHIVE = "config.tar.gz"
BIN_ARCHIVE = "bin.tar.gz"
TEST_NETWORK = "casper-test"


def pull_url(network: str, protocol: str, archive_name: str) -> str:

    if network == TEST_NETWORK:
        return f"{TEST_PULL_URL}/{network}/{protocol}/{archive_name}"
    return f"{PULL_URL}/{network}/{protocol}/{archive_name}"


def get_chainspec_config_readme(protocol: str, network: str) -> tuple:
    try:
        with TemporaryDirectory() as temp_dir:
            r = requests.get(pull_url(network, protocol, CONFIG_ARCHIVE))
            archive_path = f"{temp_dir}/{CONFIG_ARCHIVE}"
            with open(archive_path, "wb") as f:
                f.write(r.content)
            with tarfile.TarFile.open(archive_path) as tf:
                for member in tf.getmembers():
                    f = tf.extractfile(member)
                    if member.name.endswith("chainspec.toml"):
                        chainspec_toml = f.read().decode("UTF-8")
                    if member.name.endswith("config-example.toml"):
                        config_toml = f.read().decode("UTF-8")

            r = requests.get(pull_url(network, protocol, BIN_ARCHIVE))
            archive_path = f"{temp_dir}/{BIN_ARCHIVE}"
            with open(archive_path, "wb") as f:
                f.write(r.content)
            with tarfile.TarFile.open(archive_path) as tf:
                for member in tf.getmembers():
                    f = tf.extractfile(member)
                    if member.name.endswith("README.md"):
                        readme = f.read().decode("UTF-8")

        return chainspec_toml, config_toml, readme
    except Exception:
        return None, None, None
