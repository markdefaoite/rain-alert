import requests
import data


response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=data.parameters)
response.raise_for_status()
data = response.json()

print(data)


