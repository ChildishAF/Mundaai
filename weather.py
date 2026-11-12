# Import the requests library.
import requests

# Import our location coordinates.
from locations import LOCATIONS


def get_weather(location):

    # --------------------------------
    # FIND THE LOCATION
    # --------------------------------

    # Check whether the location exists
    # in our LOCATIONS dictionary.
    if location not in LOCATIONS:

        # We don't know this location yet.
        return None

    # Get the coordinates for the location.
    coordinates = LOCATIONS[location]

    # Get the latitude.
    latitude = coordinates["latitude"]

    # Get the longitude.
    longitude = coordinates["longitude"]


    # --------------------------------
    # ASK THE WEATHER API
    # --------------------------------

    # Weather API address.
    url = "https://api.open-meteo.com/v1/forecast"

    # Information we send to the API.
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,rain"
    }

    # Send the request.
    response = requests.get(url, params=params)


    # --------------------------------
    # CHECK THE RESPONSE
    # --------------------------------

    if response.status_code == 200:

        # Convert the response into a Python dictionary.
        data = response.json()

        # Get the current weather.
        current_weather = data["current"]

        # Get the temperature.
        temperature = current_weather["temperature_2m"]
        # Get the current rainfall amount.
        rain = current_weather["rain"]

        # Display the rainfall.
        print("Current rain:", rain, "mm")

        # Return the temperature.
        return temperature

    else:

        # The API request failed.
        return None


# --------------------------------
# TEST
# --------------------------------

# Ask for Masvingo's weather.
temperature = get_weather("masvingo")

# Display the result.
print("Masvingo temperature:", temperature, "°C")