import os
from google.cloud import storage

class GCSManager:
    def __init__(self, client=None):
        if client:
            self.client = client
        else:
            # Create a new GCS client if not provided
            self.client = storage.Client()

    def create_bucket(self, bucket_name, location='US'):
        try:
            bucket = self.client.create_bucket(bucket_name, location=location)
            print(f"Bucket {bucket.name} created in {bucket.location}.")
        except Exception as e:
            print(f"Error creating bucket: {e}")

    def upload_bytes(self, bucket_name, bytes_data, blob_name):
        try:
            bucket = self.client.get_bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.upload_from_file(BytesIO(bytes_data), content_type="application/json")
            print(f"Uploaded bytes data to {blob_name} in {bucket_name}.")
        except Exception as e:
            print(f"Error uploading bytes data to GCS: {e}")

def get_gcs_client():
    # Set up GCS client
    return storage.Client()

