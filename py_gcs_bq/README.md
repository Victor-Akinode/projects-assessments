##Project Title: Interacting with Google Cloud Storage (GCS) and BigQuery

#Overview:
This project demonstrates how to interact with Google Cloud Storage (GCS) and BigQuery using Python. It allows users to load data from local CSV files and an external API into BigQuery tables, as well as store JSON data fetched from the API in a GCS bucket.

#Prerequisites:
Before running the code, ensure you have the following installed:

- Python 3.x
- Google Cloud SDK
- pip package manager

#Setup:
1. Clone the repository to your local machine:
git clone <repository_url>

2. Install the required Python packages using pip:
pip install -r requirements.txt

3. Create a .env file in the project directory and define the following environment variables:
BUCKET_NAME=<your_bucket_name>
DATASET_ID=<your_dataset_id>
CSV_TABLE_ID=<your_csv_table_id>
API_URL=<your_api_url>
GCS_BLOB_NAME=<your_blob_name>

4. Update the environment variables with your specific values.
project_root/
│
├── main.py
├── api_loader.py
├── gcs_manager.py
├── bigquery_manager.py
├── data/
│   └── autos.csv
│
└── README.md

`main.py`: The main script to execute the project.
`api_loader.py`: Module to fetch data from an external API.
`gcs_manager.py`: Module to interact with Google Cloud Storage.
`bigquery_manager.py`: Module to interact with Google BigQuery.
`data/`: Directory to store input data files.
`README.md`: Documentation file.

#Usage:
1. Ensure the prerequisites are met and the environment variables are properly configured.
2. Run the main.py script to execute the project:

python main.py

3. Monitor the terminal for any error messages or status updates during the execution.


Functionality:
1. Loading local CSV data into BigQuery:

- The main.py script loads data from a local CSV file (data/autos.csv) into a specified BigQuery table.
- The bigquery_manager.py module handles the interaction with BigQuery.

2. Fetching data from an external API and storing it in GCS:

- The api_loader.py module fetches JSON data from an external API specified in the .env file.
- The fetched data is then stored in a GCS bucket specified in the .env file using the gcs_manager.py module.

#Troubleshooting:
If you encounter any issues during setup or execution, consider the following troubleshooting steps:

Double-check the environment variables in the .env file for correctness.
Ensure the required Python packages are installed and up-to-date.
Check for any error messages in the terminal and refer to the project's documentation for guidance.
Contributors:
Victor Akinode



