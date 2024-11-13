import requests
# POST request to add new data
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={
    "title": "foo",
    "body": "bar",
    "userId": 1
    }
)

print("POST Response:", response.json())