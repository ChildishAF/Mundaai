# This function checks whether MundaAI has
# all the information needed to answer the farmer.
def check_missing_information(intent, entities):

    # Get the crop from our entities dictionary.
    crop = entities["crop"]

    # Get the location.
    location = entities["location"]

    # Get the market.
    market = entities["market"]


    # -------------------------
    # WEATHER
    # -------------------------

    # To give weather information,
    # we need to know the farmer's location.
    if intent == "WEATHER":

        if location is None:
            return "Please tell me your location."

    
    # -------------------------
    # PLANTING ADVICE
    # -------------------------

    # Planting advice needs both:
    # 1. The crop
    # 2. The farmer's location
    elif intent == "PLANTING_ADVICE":

        if crop is None:
            return "Which crop do you want to plant?"

        if location is None:
            return "Please tell me your farming location."


    # -------------------------
    # MARKET PRICE
    # -------------------------

    # For a market price, we need to know
    # which crop the farmer is asking about.
    elif intent == "MARKET_PRICE":

        if crop is None:
            return "Which crop's price do you want?"

        # The farmer can give us either:
        # a specific market OR a location.
        if market is None and location is None:
            return "Which market or location should I check?"


    # -------------------------
    # EVERYTHING IS AVAILABLE
    # -------------------------

    # If none of the checks above found
    # missing information, we can continue.
    return None