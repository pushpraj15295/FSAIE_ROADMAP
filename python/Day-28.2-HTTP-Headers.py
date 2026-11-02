# HTTP Headers -----------------------------------------------

# HTTP headers are a way for servers to tell clients about the request and response.
# They are a key-value pair that contains additional information about the request or response.

# For example:
# GET /users/1 HTTP/1.1
# Host: jsonplaceholder.typicode.com
# Accept: application/json
# User-Agent: Python-requests/2.25.1

# The headers are sent in the request and response.

# The headers are used to tell the server about the client's preferences.

import requests

# api.example.com is documentation-only; use a real practice API:
url = "https://jsonplaceholder.typicode.com/users/1"

headers = {
    "Accept": "application/json",
    "User-Agent": "FSAIE-Learning-Script/1.0",
    # Real APIs often need a token; JSONPlaceholder ignores this for practice:
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
}

response = requests.get(url, headers=headers, timeout=10)

print(response.status_code)
print("Response Content-Type:", response.headers.get("Content-Type"))
print(response.json())
print(response.text)