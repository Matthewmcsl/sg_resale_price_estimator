import logging
import yaml


# Configure logging parameters
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_config(file_path="../config.yaml"):
    logging.info("Loading configs from file.")
    with open(file_path, "r") as f:
        config = yaml.safe_load(f)
    logging.info("Configs loaded successfully")
    return config
