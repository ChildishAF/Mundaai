# Import FastAPI so we can create our API.
from fastapi import FastAPI

# Import the function that determines the farmer's intent.
from intent import detect_intent

# Import the function that extracts crop and location.
from entities import extract_entities
from requirements import check_missing_information
from conversation import (
    update_conversation,
    get_conversation,
    set_waiting_for,
    clear_waiting_for,
    use_answer
)
from farmer import update_farmer_profile, get_farmer_profile


# Create the FastAPI application.
app = FastAPI()


# Home endpoint.
@app.get("/")
def home():

    # Return a welcome message.
    return {"message": "Welcome to MundaAI 🌱"}


# Farmer question endpoint.
@app.get("/ask")
def ask_mundaai(message: str):

    # --------------------------------
    # STEP 1: DETECT INTENT
    # --------------------------------

    # Try to understand what the farmer wants.
    intent = detect_intent(message)


    # --------------------------------
    # STEP 2: EXTRACT ENTITIES
    # --------------------------------

    # Look for crops, locations and markets
    # in the farmer's message.
    entities = extract_entities(message)


    # --------------------------------
    # STEP 3: CHECK EXISTING CONVERSATION
    # --------------------------------

    # Get what MundaAI already remembers.
    memory = get_conversation()


    # --------------------------------
    # STEP 4: HANDLE A FOLLOW-UP ANSWER
    # --------------------------------

    # If the new message doesn't contain a
    # recognizable intent, it might be an answer
    # to something MundaAI previously asked for.
    if intent == "UNKNOWN" and memory["waiting_for"] is not None:

        # Give the new information to our
        # conversation memory.
        use_answer(entities)

        # Get the updated memory.
        memory = get_conversation()

        # Use the remembered intent instead of UNKNOWN.
        intent = memory["intent"]


    # --------------------------------
    # STEP 5: UPDATE CONVERSATION
    # --------------------------------

    # Save any new information we found.
    update_conversation(entities, intent)

    # Get the latest conversation memory.
    memory = get_conversation()
    # Save useful information to the farmer's profile.
    update_farmer_profile(
             location=memory["location"],
             crop=memory["crop"]
             )

    # Get the updated memory again.
    memory = get_conversation()


    # --------------------------------
    # STEP 6: CHECK MISSING INFORMATION
    # --------------------------------

    # Check whether MundaAI has everything
    # required to answer the farmer.
    missing_information = check_missing_information(
        memory["intent"],
        memory
    )


    # --------------------------------
    # STEP 7: REMEMBER WHAT WE NEED
    # --------------------------------

    # If information is missing, remember
    # what we need from the farmer.
    if missing_information is not None:

        # For now, we specifically handle
        # a missing location.
        if "location" in missing_information.lower():

            set_waiting_for("LOCATION")


    # --------------------------------
    # STEP 8: RETURN EVERYTHING
    # --------------------------------

    return {
    "message": message,
    "intent": memory["intent"],
    "entities": memory,
    "missing_information": missing_information,

    # Show what MundaAI remembers about the farmer.
    "farmer_profile": get_farmer_profile()
}