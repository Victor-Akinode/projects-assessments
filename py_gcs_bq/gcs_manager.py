from google.cloud import storage

class GCSManager:
    def __init__(self, client=None):
        self.client = client or storage.Client()

    def create_bucket(self, bucket_name):
        bucket = self.client.bucket(bucket_name)
        if not bucket.exists():
            bucket = self.client.create_bucket(bucket_name)
            print(f"Bucket {bucket_name} created.")
        else:
            print(f"Bucket {bucket_name} already exists.")
        return bucket

    def upload_json(self, bucket_name, source_data, destination_blob_name):
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_string(source_data, content_type='application/json')
        print(f"Data uploaded to {destination_blob_name} in bucket {bucket_name}.")
