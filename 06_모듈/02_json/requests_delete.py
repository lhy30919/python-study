import requests

# DELETE Method 요청
url = "https://jsonplaceholder.typicode.com/users/1"
resp = requests.delete(url)
print(resp.text)
