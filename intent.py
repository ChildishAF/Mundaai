def detect_intent(message):
    message = message.lower()

    if "price" in message:
        return "MARKET_PRICE"

    elif "rain" in message or "weather" in message:
        return "WEATHER"

    elif "plant" in message:
        return "PLANTING_ADVICE"

    else:
        return "UNKNOWN"


# Test our function with a farmer's question.
result = detect_intent("maize price harare")

# Print the result to the terminal.
print(result)