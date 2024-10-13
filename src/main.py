# src/main.py

from data.dataloader import load_config, load_data_from_api


def main():
    config = load_config()
    datasetid = config["api"]["gov_sg_resale_datasetid"]
    df = load_data_from_api(datasetid)


if __name__ == "__main__":
    main()
