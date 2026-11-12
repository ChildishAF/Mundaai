# -------------------------
# CROPS
# -------------------------

# Crops that MundaAI currently recognizes.
CROPS = [
    "maize",
    "beans",
    "tomato",
    "potato",
    "groundnuts",
    "sorghum",
    "millet",
    "cotton",
    "tobacco",
    "onion",
    "cabbage"
]


# -------------------------
# LOCATIONS
# -------------------------

# Zimbabwe locations that our prototype recognizes.
LOCATIONS = [
    "harare",
    "masvingo",
    "bulawayo",
    "mutare",
    "gweru",
    "chitungwiza",
    "marondera",
    "chinhoyi",
    "bindura",
    "kadoma",
    "kwekwe",
    "zvishavane",
    "victoria falls",
    "mashonaland",
    "manicaland",
    "matabeleland",
    "midlands"
]


# -------------------------
# MARKETS
# -------------------------

# Each market is connected to its city.
# This lets MundaAI understand that a market
# belongs to a particular location.
MARKETS = {
    "mbare": {
        "name": "Mbare",
        "city": "harare"
    },

    "makoni": {
        "name": "Makoni",
        "city": "makoni"
    }
}


# -------------------------
# ENTITY EXTRACTION
# -------------------------

def extract_entities(message):
    """
    Look through the farmer's message and identify
    crops, locations and markets.
    """

    # Convert everything to lowercase.
    message = message.lower()

    # Start with nothing found.
    crop = None
    location = None
    market = None

    # -------------------------
    # FIND THE CROP
    # -------------------------

    for possible_crop in CROPS:

        if possible_crop in message:
            crop = possible_crop
            break

    # -------------------------
    # FIND THE LOCATION
    # -------------------------

    for possible_location in LOCATIONS:

        if possible_location in message:
            location = possible_location
            break

    # -------------------------
    # FIND THE MARKET
    # -------------------------

    for possible_market in MARKETS:

        if possible_market in message:

            # Get the market's information.
            market = MARKETS[possible_market]

            break

    # -------------------------
    # RETURN THE RESULTS
    # -------------------------

    return {
        "crop": crop,
        "location": location,
        "market": market
    }


# -------------------------
# TEST
# -------------------------

result = extract_entities("what is the price of maize in Mbare?")

print(result)