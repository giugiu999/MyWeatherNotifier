import requests
import os

def get_weather():
    ip_data = requests.get("https://ipinfo.io/json").json()
    city = ip_data.get("city", "Unknown")
    loc = ip_data.get("loc", "0,0")
    lat, lon = loc.split(",")

    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = os.getenv("API_KEY")

    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"
    }

    weather_data = requests.get(url, params=params).json()

    if weather_data.get("cod") != 200:
        return city, None, None

    temp = weather_data["main"]["temp"]
    condition = weather_data["weather"][0]["description"]

    return city, temp, condition
