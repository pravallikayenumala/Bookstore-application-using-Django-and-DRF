import requests

url = 'http://127.0.0.1:8000/accounts/api/bookstore-post/'
token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwNjA0NTMyLCJpYXQiOjE2ODA2MDA4MzgsImp0aSI6IjRhNTRkMmE2YzkyNjRhMjQ5NjE4ZmU2ODNkNDI3N2ViIiwidXNlcl9pZCI6NiwidXNlcm5hbWUiOiJrcml0aGkifQ.p3xCL83ydkpZyICAvatZnAA1Nm2p8NNbYoFWH9vxLa0'

headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
}

response = requests.get(url, headers=headers)
print(response.json())