# IP API & weather API example

import requests

#IP API
response = requests.get("https://ipinfo.io/json")
data = response.json()

city = data.get("city")   
loc = data.get("loc")  

lat, lon = loc.split(",")
print(f"City: {city}, Latitude: {lat}, Longitude: {lon}")

# weather API(latitude and longitude)
url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "d81b485530589e3c8b3d642f205b2c1d"   # replace with your real API key

params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "units": "metric"
}

weather_response = requests.get(url, params=params)
weather_data = weather_response.json()

# extract info
temp = weather_data["main"]["temp"]
condition = weather_data["weather"][0]["description"]

print(f"City: {city}")
print(f"Temperature: {temp}°C")
print(f"Condition: {condition}")
