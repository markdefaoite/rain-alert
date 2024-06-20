import requests
import data
from twilio.rest import Client


response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=data.parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(data.account_sid, data.auth_token)
    message = client.messages.create(
        from_= data.from_number,
        body="it's going to rain today! remember to bring an umbrella 🌧️☔",
        to= data.to_number
    )
print(message.status)
