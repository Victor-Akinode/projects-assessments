from google.cloud import bigquery

class BigQueryManager:
    def __init__(self, client=None):
        self.client = client or bigquery.Client()

    def create_dataset(self, dataset_id, location='US'):
        dataset_ref = self.client.dataset(dataset_id)
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = location
        try:
            self.client.get_dataset(dataset_ref)
            print(f"Dataset {dataset_id} already exists in {location}.")
        except:
            dataset = self.client.create_dataset(dataset)
            print(f"Dataset {dataset_id} created in {location}.")
        return dataset

    def load_csv_to_table(self, dataset_id, table_id, source_file_name):
        table_ref = self.client.dataset(dataset_id).table(table_id)
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            autodetect=True,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        )
        with open(source_file_name, 'rb') as source_file:
            job = self.client.load_table_from_file(source_file, table_ref, job_config=job_config)

        job.result()
        print(f"Loaded {job.output_rows} rows into {dataset_id}:{table_id}.")

    def load_json_to_table(self, dataset_id, table_id, source_uri, schema_file):
        dataset_ref = self.client.dataset(dataset_id)
        table_ref = dataset_ref.table(table_id)
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            schema=schema_file,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        )
        load_job = self.client.load_table_from_uri(source_uri, table_ref, job_config=job_config)
        load_job.result()
        print(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}.")
