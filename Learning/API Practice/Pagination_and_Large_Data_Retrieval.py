import requests

url = "https://api.github.com/users/vcovelli/repos" # Change 'vcovelli' with GitHub {username}
repos = []
page = 1 

while True:
    response = requests.get(url, params={"page": page, "per_page": 10})
    data = response.json()
    if not data: # If no more pages, break the Loop
        break
    repos.extend(data)
    page += 1

print("Total repositories fetched:", len(repos))    