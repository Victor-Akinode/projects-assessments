import os
from dotenv import load_dotenv
import json
from api_loader import APILoader
from gcs_manager import GCSManager, get_gcs_client

load_dotenv()

BUCKET_NAME = os.getenv("BUCKET_NAME")
API_URL = os.getenv("API_URL")
GCS_BLOB_NAME = os.getenv("GCS_BLOB_NAME")

def main():
    # Initialize GCS client and manager
    gcs_client = get_gcs_client()
    gcs_manager = GCSManager(client=gcs_client)

    # Initialize API loader
    api_loader = APILoader(API_URL)

    # Fetch data from API
    json_data = api_loader.fetch_data()

    # Convert JSON data to bytes
    json_bytes = json.dumps(json_data).encode('utf-8')

    # Upload JSON data to GCS
    gcs_manager.upload_bytes(BUCKET_NAME, json_bytes, GCS_BLOB_NAME)

if __name__ == "__main__":
    main()
