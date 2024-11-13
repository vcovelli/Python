import requests

class APIError(Exception):
    pass

class RateLimitError(APIError):
    pass

def fetch_data(url, params):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        raise RateLimitError("Rate limit exceeded")
    elif response.status_code == 404:
        raise APIError("Resource not found")
    else:
        raise APIError("Failed to fetch data")