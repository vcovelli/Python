import os
import requests

api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    print("API key is missing!")
else:    
    url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}"
    response = requests.get(url)
    print("Response:", response.json())