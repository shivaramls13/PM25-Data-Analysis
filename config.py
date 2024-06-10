# Configuration settings for the application

# API endpoint template for fetching device history data
API_URL = "https://pm25.lass-net.org/API-1.0.0/device/{device_id}/history/?format=JSON"

# Device ID for the AirBox device
DEVICE_ID = "74DA38F210A2"

# Path to the SQLite database file
DB_PATH = "pm25_data.db"

# PM2.5 threshold level for danger alerts
PM25_THRESHOLD = 30
