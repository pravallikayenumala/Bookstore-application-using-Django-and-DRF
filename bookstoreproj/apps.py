import requests

url =  'http://127.0.0.1:8000/accounts/api/bookstore-post/'
token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwNjEzOTQxLCJpYXQiOjE2ODA2MTAzNDEsImp0aSI6IjM2MGJiYTU2ZTIzOTQ2MzZhMjhkYzRkNDRmMGM3OGU2IiwidXNlcl9pZCI6NiwidXNlcm5hbWUiOiJrcml0aGkifQ.SzB687fF9i-YpfBkuvkugH7j0MYfVgGm12DLOxH3-hQ'
headers = {
    'Authorization': token,
    'Content-Type': 'application/json',
}

response = requests.get(url, headers=headers)
print(response.json())