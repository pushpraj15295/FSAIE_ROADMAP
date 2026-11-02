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