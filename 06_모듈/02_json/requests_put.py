import requests

# PUT Method 요청
url = "https://jsonplaceholder.typicode.com/users/1"
json_data = {"name": "Bob"}
resp = requests.put(url, json=json_data)
print(resp.text)
