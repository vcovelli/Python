import requests
import time

def get_data_with_retries(url, params, retries=3):
    for attempt in range(retries):
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            print("Rate limited. Retrying...")
            time.sleep(2 ** attempt) # Exponential backoff
    return None  

# Example usage:
url = "https://api.yourservice.com/data" # Replace with a real API URL
params = {"key": "value"} # Replace with actual query parameters

data = get_data_with_retries(url, params)
if data:
    print("Data retrieved successfully:", data)
else:
    print("Failed to retrieve data after multiple attempts.")    