# src/main.py

from data.dataloader import load_data_from_api
from config import load_config


def main():
    config = load_config()
    datasetid = config["api"]["gov_sg_resale_datasetid"]
    df = load_data_from_api(datasetid)


if __name__ == "__main__":
    main()
