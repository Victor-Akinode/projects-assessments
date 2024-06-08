import requests
import json

class APILoader:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        response = requests.get(self.api_url)
        response.raise_for_status()
        return response.json()

    def fetch_data_as_jsonl(self):
        data = self.fetch_data()
        jsonl_data = "\n".join([json.dumps(record) for record in data])
        return jsonl_data
