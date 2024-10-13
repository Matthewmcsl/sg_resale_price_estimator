"""
dataloader.py

This module provides functions for querying resale data directly from
GOV SG's API into a pandas dataframe.
"""

import time
from requests import get
import pandas as pd
import logging


def load_data_from_api(datasetID: str):
    """
    Function fetches the specific dataset, as idenfitied by Dataset ID
    from data.gov.sg, and returns in a pandas dataframe format
    """
    logging.info(f"Fetching data from Data GOV API, datasetid :{datasetID}...")
    start_time = time.time()

    try:
        response = get(
            f"https://api-open.data.gov.sg/v1/public/api/datasets/{datasetID}/initiate-download",
            headers={"Content-Type": "application/json"},
            json={},
        )

        response.raise_for_status()
        logging.info(f"API response status code: {response.status_code}")
        logging.info(
            f"Time taken to get API call response: {(time.time()-start_time):2f} seconds."
        )

        api_data = response.json()["data"]["url"]
        api_df = pd.read_csv(api_data)

        # if dataframe is empty, nothing was loaded
        if api_df.empty:
            logging.warning("No data was loaded from the API call.")
        else:
            logging.info(f"Dataframe of size {len(api_df)} was loaded.")

        logging.info("Data fetching and loading successfully completed.")
        return api_df

    except Exception as e:
        # log issue and include traceback error with exc_info=True
        logging.error("Error occured while fetching/loading data.", exc_info=True)
