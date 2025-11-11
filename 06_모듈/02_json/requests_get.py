import requests

# GET Method 요청
url = "https://jsonplaceholder.typicode.com/users"
resp = requests.get(url)
print(resp.text)
print(resp.status_code)
print(resp.json())
