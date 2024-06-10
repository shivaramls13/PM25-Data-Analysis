import requests
import logging
from config import API_URL, DEVICE_ID

def fetch_data():
    """
    Fetch data from the API for the specified device.
    """
    url = API_URL.format(device_id=DEVICE_ID)
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an error for bad HTTP status codes
        return response.json() # Return the response data in JSON format
    except requests.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        raise
