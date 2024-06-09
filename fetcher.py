import requests
import logging
from config import API_URL, DEVICE_ID

def fetch_data():
    url = API_URL.format(device_id=DEVICE_ID)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        raise
