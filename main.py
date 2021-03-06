import os

import requests
from twilio.rest import Client

account_sid = "ACdc16ce57c4532d91713a090d2babe7f3"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
print(auth_token)

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
print(api_key)

weather_params = {
    "lat": "5.15",
    "lon": "112.19",
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()

will_rain = False
weather_slice = response.json()["hourly"][:12]
for hour_data in weather_slice:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="Bring an umbrella.",
                         from_='+19894798012',
                         to='+32475862631'
                     )
    print(message.status)
