# Import the requests library.
import requests

# Import our Zimbabwe locations.
from locations import LOCATIONS


# --------------------------------
# GET 7-DAY FORECAST
# --------------------------------

def get_forecast(location):

    # Check whether we know this location.
    if location not in LOCATIONS:

        # We don't have coordinates for it yet.
        return None


    # Get the coordinates for the location.
    coordinates = LOCATIONS[location]

    # Get latitude.
    latitude = coordinates["latitude"]

    # Get longitude.
    longitude = coordinates["longitude"]


    # --------------------------------
    # WEATHER API
    # --------------------------------

    # Open-Meteo API address.
    url = "https://api.open-meteo.com/v1/forecast"


    # Information we send to the API.
    params = {

        "latitude": latitude,

        "longitude": longitude,

        # Ask for these three pieces
        # of daily weather information.
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",

        # Use Zimbabwe's timezone.
        "timezone": "Africa/Harare",

        # Get 7 days.
        "forecast_days": 7
    }


    # Send the request to the API.
    response = requests.get(url, params=params)


    # --------------------------------
    # CHECK RESPONSE
    # --------------------------------

    if response.status_code != 200:

        # Something went wrong.
        return None


    # Convert JSON into a Python dictionary.
    data = response.json()


    # Get the daily forecast.
    daily = data["daily"]


    # --------------------------------
    # EXTRACT THE INFORMATION
    # --------------------------------

    dates = daily["time"]

    max_temperatures = daily["temperature_2m_max"]

    min_temperatures = daily["temperature_2m_min"]

    rain_probabilities = daily["precipitation_probability_max"]


    # --------------------------------
    # BUILD OUR FORECAST
    # --------------------------------

    forecast = []


    # Go through each of the 7 days.
    for i in range(7):

        # Create one dictionary for this day.
        day = {
            "date": dates[i],
            "max_temperature": max_temperatures[i],
            "min_temperature": min_temperatures[i],
            "rain_probability": rain_probabilities[i]
        }

        # Add this day's information
        # to our forecast list.
        forecast.append(day)


    # Return the complete forecast.
    return forecast


# --------------------------------
# TEST
# --------------------------------

result = get_forecast("masvingo")

print(result[0])

date = result[0]["date"]
max_temp = result[0]["max_temperature"]
min_temp = result[0]["min_temperature"]
rain = result[0]["rain_probability"]

print(
    "On", date,
    "the temperature will be between",
    min_temp, "and", max_temp,
    "°C, with a", rain,
    "% chance of rain."
)