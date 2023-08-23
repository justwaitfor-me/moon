import requests
response = requests.get('https://eu.api.riotgames.com/val/content/v1/contents')
data = response.json()
print(str(data))

