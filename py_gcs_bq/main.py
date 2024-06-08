import os
from config import (
    GOOGLE_APPLICATION_CREDENTIALS,
    API_URL,
    BUCKET_NAME,
    DATASET_ID,
    CSV_TABLE_ID,
    JSON_TABLE_ID,
    get_gcs_client,
    get_bigquery_client
)
from gcs_manager import GCSManager
from bigquery_manager import BigQueryManager
from api_loader import APILoader

def main():
    # Set up Google Cloud credentials
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS

    # Initialize managers
    gcs_manager = GCSManager(client=get_gcs_client())
    bq_manager = BigQueryManager(client=get_bigquery_client())
    api_loader = APILoader(api_url=API_URL)

    # Create GCS bucket
    gcs_manager.create_bucket(BUCKET_NAME)

    # Create BigQuery dataset
    bq_manager.create_dataset(DATASET_ID)

    # Task 1: Load CSV to BigQuery
    csv_file_path = 'py_gcs_bq/data/autos.csv'
    bq_manager.load_csv_to_table(DATASET_ID, CSV_TABLE_ID, csv_file_path)

    # Task 2: Load data from API to GCS and BigQuery
    json_data = api_loader.fetch_data_as_jsonl()
    gcs_blob_name = 'api_data.jsonl'
    gcs_manager.upload_json(BUCKET_NAME, json_data, gcs_blob_name)

    source_uri = f'gs://{BUCKET_NAME}/{gcs_blob_name}'
    schema_file = 'py_gcs_bq/schemas/schema.json'  # Define your schema here
    bq_manager.load_json_to_table(DATASET_ID, JSON_TABLE_ID, source_uri, schema_file)

if __name__ == "__main__":
    main()
