import requests 

# Define the API endpoint
url = "https://api.coingecko.com/api/v3/simple/price"
parameters = {
    "ids": "bitcoin,ethereum", # Cryptos to fetch
    "vs_currencies": "usd"      # Currency to display prices in
}

# Make the GET request
response = requests.get(url, params=parameters)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print("Bitcoin Price (USD):", data.get("bitcoin", {}).get("usd"))
    print("Ethereum Price (USD):", data.get("ethereum", {}).get("usd"))
else:
    print("Failed to retrieve data:", response.status_code)    