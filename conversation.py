# This dictionary represents the information
# MundaAI remembers about the conversation.
conversation = {
    "intent": None,
    "crop": None,
    "location": None,
    "market": None,
    "waiting_for": None
}


def update_conversation(entities, intent):

    conversation["intent"] = intent

    if entities["crop"] is not None:
        conversation["crop"] = entities["crop"]

    if entities["location"] is not None:
        conversation["location"] = entities["location"]

    if entities["market"] is not None:
        conversation["market"] = entities["market"]


def set_waiting_for(information):

    conversation["waiting_for"] = information


def clear_waiting_for():

    conversation["waiting_for"] = None


def use_answer(entities):

    # Find out what information we are waiting for.
    waiting_for = conversation["waiting_for"]

    # If we're waiting for a location and
    # the farmer gave us one...
    if waiting_for == "LOCATION" and entities["location"] is not None:

        # Save the location.
        conversation["location"] = entities["location"]

        # Stop waiting for it.
        clear_waiting_for()


def get_conversation():

    return conversation