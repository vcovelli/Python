import requests 

# Define the API endpoint
url = "https://newsapi.org/v2/everything"
parameters = {
    "q": "finance",
    "apiKey": "cea058b392224fcc824c5635f6f1e6af",
    "pageSize": 10
}

# Make the GET request
response = requests.get(url, params=parameters)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    articles = data.get("articles", [])
    print("Total Articles:", len(articles))
    for article in articles[:5]:
        print(f"Title: {article['title']}")
else:
    print("Failed to retrieve data:", response.status_code)    