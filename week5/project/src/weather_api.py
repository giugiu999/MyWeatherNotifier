import requests
import os
import logging

def get_weather():
    """
    Fetch current weather for the user's city (auto-detected via IP).

    Uses OpenWeatherMap's Current Weather endpoint and returns a triple:
    (city, temperature_celsius, description)

    Returns (city, None, None) on failure with friendly, logged messages.
    """

    # Determine location by IP. try/except guards against network issues.
    try:
        logging.info("Fetching location from ipinfo.io...")
        ip_response = requests.get("https://ipinfo.io/json", timeout=10)
        ip_response.raise_for_status()
        ip_data = ip_response.json()
    except requests.exceptions.RequestException:
        # try: marks a risky block. except: catches errors so the program can continue.
        logging.error("Could not determine location — check your internet connection.")
        return "Unknown", None, None

    city = ip_data.get("city", "Unknown")
    loc = ip_data.get("loc", "0,0")
    try:
        lat, lon = loc.split(",")
    except ValueError:
        logging.error("Location format unexpected. Unable to parse latitude/longitude.")
        return city, None, None

    # Support both API_KEY (per README) and WEATHER_API (legacy) environment names
    api_key = os.getenv("API_KEY") or os.getenv("WEATHER_API")
    if not api_key:
        logging.error("API key missing — set API_KEY in your .env file.")
        return city, None, None

    # Use the Current Weather endpoint which returns main.temp and weather[0].description
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric",
    }

    try:
        logging.info(f"Fetching weather for {city}...")
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        weather_data = response.json()
    except requests.exceptions.HTTPError:
        logging.error("Could not fetch weather — check city/coordinates or your API key.")
        return city, None, None
    except requests.exceptions.RequestException:
        logging.error("Network error while fetching weather — try again later.")
        return city, None, None

    try:
        temp = weather_data["main"]["temp"]
        condition = weather_data["weather"][0]["description"]
    except (KeyError, TypeError):
        logging.error("Unexpected weather response format from API.")
        return city, None, None

    return city, temp, condition
