import os
from dotenv import load_dotenv
from google.cloud import storage, bigquery

load_dotenv()

GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
API_URL = os.getenv('API_URL')
BUCKET_NAME = os.getenv('BUCKET_NAME')
DATASET_ID = os.getenv('DATASET_ID', 'etl_basics')
CSV_TABLE_ID = os.getenv('CSV_TABLE_ID')
JSON_TABLE_ID = os.getenv('JSON_TABLE_ID')

def get_gcs_client():
    return storage.Client()

def get_bigquery_client():
    return bigquery.Client()
