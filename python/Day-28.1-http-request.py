# HTTP request is a request sent by a client to a server.
#  HTTP (Hypertext Transfer Protocol) is a communication protocol that allows 
# two systems to exchange information over a network.


# In simple terms:
# - Request = Client asks the server for something.
# - Response = Server sends information back.

# HTTP is the communication protocol. HTTPS is HTTP protected by TLS encryption.

# What is an HTTP Request? -----------------------------------------------

# For example  -
# GET https://api.example.com/users
# (example.com is only a placeholder in docs — it is not a real API host.)
# Below we use JSONPlaceholder, a free fake REST API for practice.

# An HTTP request commonly contains:
# - Method: What action you want to perform
# - URL: Where you want to send the request
# - Headers: Additional information about the request
# - Body: Data you want to send (when needed)




# HTTP Methods -----------------------------------------------
# These are the most commonly used methods:

# - GET: Retrieve data
# - POST: Create or submit data
# - PUT: Replace a resource
# - PATCH: Partially update
# - DELETE: Delete a resource


# example:

import requests

url = "https://jsonplaceholder.typicode.com/users/1"
res = requests.get(url, timeout=10)

print(res.status_code)
print(res.headers.get("Content-Type"))
print(res.json()) # convert the response to a JSON object
print(res.text) # convert the response to a string



# What are HTTP Status Codes? -----------------------------------------------

# HTTP status codes are a way for servers to tell clients whether a request was successful or not.
# They are a 3-digit number that indicates the status of the response.

# There are five main status code categories : 

# 1xx: Informational - The request was received, continuing process
# The request is still being processed or negotiated

# 2xx: Success - The request was successful
# 200 — OK
# 201 — Created
# 204 — No Content

# 3xx: Redirection - The request was redirected
# 301 — Moved Permanently
# 302 — Found (temporary redirect)
# 304 — Not Modified

# 4xx: Client Error - The request was invalid
# 400 — Bad Request
# 401 — Unauthorized (authentication required)
# 403 — Forbidden
# 404 — Not Found
# 409 — Conflict
# 422 — Unprocessable Content


# 5xx: Server Error - The server was not able to handle the request
# 500 — Internal Server Error
# 502 — Bad Gateway
# 503 — Service Unavailable


import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

if response.status_code == 200:
    print("User found! successfully")
    print(response.json())

elif response.status_code == 404:
    print("User not found")

else:
    print("Something went wrong")
