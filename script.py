import requests

response = requests.get('http://0.0.0.0:8000/v1/status')

response = response.json()

print(response)