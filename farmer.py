# --------------------------------
# FARMER PROFILE
# --------------------------------

# For now, we will store one farmer's
# information in a Python dictionary.
#
# Later, this information will live
# inside our database.
farmer = {
    "phone": None,
    "language": "English",
    "location": None,
    "crops": []
}


def update_farmer_profile(location=None, language=None, crop=None):
    """
    Update information about the farmer.
    """

    # If we received a location,
    # save it to the farmer's profile.
    if location is not None:
        farmer["location"] = location

    # If we received a language,
    # save it to the farmer's profile.
    if language is not None:
        farmer["language"] = language

    # If we received a crop,
    # add it to the farmer's crop list.
    if crop is not None:

        # Only add the crop if we don't
        # already have it in the list.
        if crop not in farmer["crops"]:
            farmer["crops"].append(crop)


def get_farmer_profile():
    """
    Return the farmer's saved information.
    """

    return farmer

# --------------------------------
# TEST
# --------------------------------

# Save Masvingo as the farmer's location.
update_farmer_profile(
    location="masvingo"
)

# Save maize as one of the farmer's crops.
update_farmer_profile(
    crop="maize"
)

# Display the farmer's profile.
print(get_farmer_profile())