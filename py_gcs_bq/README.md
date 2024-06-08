###PROJECT STRUCTURE

py_gcs_bq/
├── .env.example
├── config.py
├── gcs_manager.py
├── bigquery_manager.py
├── api_loader.py
├── main.py
├── README.md


# GCP Data Manager

## Overview
This project allows users to:
1. Load CSV files from their local machine directly into a Google BigQuery table.
2. Load data from an API into a GCS bucket as JSON/JSONL and then into a BigQuery table.

## Prerequisites
- Python 3.7+
- Google Cloud SDK
- A Google Cloud project with BigQuery and GCS enabled
- Service account with appropriate permissions

## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd py_gcs_bq
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file:**
    Copy the `.env.example` file to `.env` and fill in the required values.

    ```sh
    cp .env.example .env
    ```

    Update the `.env` file with your actual values.

5. **Run the main script:**
    ```sh
    python main.py
    ```

## Environment Variables
The following environment variables need to be set in the `.env` file:

- `GOOGLE_APPLICATION_CREDENTIALS`: Path to your service account JSON key file.
- `API_URL`: URL of the API to fetch data from.
- `BUCKET_NAME`: Name of the GCS bucket.
- `DATASET_ID`: ID of the BigQuery dataset (default: `etl_basics`).
- `CSV_TABLE_ID`: ID of the BigQuery table for CSV data.
- `JSON_TABLE_ID`: ID of the BigQuery table for JSON data.

## License
MIT License
