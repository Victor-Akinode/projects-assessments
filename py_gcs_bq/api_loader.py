import requests

class APILoader:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
            if response.status_code == 200:
                print("API response:", response.text)
                return response.json()
            else:
                print(f"API returned status code {response.status_code}.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return None
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return None
