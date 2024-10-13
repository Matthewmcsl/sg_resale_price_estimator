# # tests/test_dataloader.py

# """
# Module tests if api call is success
# """

# import os
# import sys

# from unittest.mock import patch

# # Add the src directory to sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# from src.data.dataloader import load_data_from_api

# datasetId = "d_8b84c4ee58e3cfc0ece0d773c8ca6abc"
# sample_gov_api_url = (
#     "https://data.gov.sg/api/action/datastore_search?resource_id=" + datasetId
# )


# def test_load_data_from_api_success(mocker):
#     # Mock the requests.get call to return a successful response
#     mock_response = mocker.patch("requests.get")
#     mock_response.return_value.status_code = 200

#     # Call the function with the test URL
#     df = load_data_from_api(sample_gov_api_url)

#     # Assertions
#     assert df is not None, "DataFrame should not be None"
#     assert df.shape == (100, 11), "DataFrame should have 100 rows and 11 columns"
