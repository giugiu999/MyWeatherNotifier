"""
This module demonstrates how to interact with real-world web APIs using Python.
We use the OpenWeatherMap API to fetch and display the current temperature for a user-provided city.

Concepts covered:
1. Making an API request using requests.
2. Parsing JSON responses.
3. Extracting temperature and converting it from Kelvin to Celsius.
4. Creating a reusable function get_weather(city).
"""

import requests

# Replace with your actual API key from OpenWeatherMap
API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def fetch_weather_data(city):
    """
    Sends an HTTP GET request to the OpenWeatherMap API for the given city.
    """
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}"
        response = requests.get(url)

        # Raise an HTTPError for status codes
        response.raise_for_status()

        # Parse and return JSON data
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

    return None


def parse_temperature(weather_data):
    """
    Extracts the temperature from the weather data and converts it from Kelvin to Celsius.
    """
    try:
        # extract value from json
        temp_kelvin = weather_data['main']['temp']
        temp_celsius = temp_kelvin - 273.15  # Convert Kelvin to Celsius
        return round(temp_celsius, 1)
    except (KeyError, TypeError):
        print("Failed to parse temperature data.")
        return None


def get_weather(city):
    """
    Fetches and summarizes the current weather for a given city.
    """
    weather_data = fetch_weather_data(city)
    if not weather_data:
        return f"Unable to fetch weather for {city}."

    temp = parse_temperature(weather_data)
    if temp is None:
        return f"Weather data for {city} is unavailable."

    return f"Current temperature in {city} is {temp}°C."


if __name__ == "__main__":
    # Example usage
    city_name = input("Enter a city name: ")
    result = get_weather(city_name)
    print(result)
