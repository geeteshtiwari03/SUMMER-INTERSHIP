import requests

url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url)

data = response.json()

print("Dog Image URL:")
print(data["message"])