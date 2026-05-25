def get_season_advice(season):
    """Return gardening advice based on the season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """Return gardening advice based on the plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """Combine advice from both functions and print it."""
    season = "summer"        # still hardcoded for Issue 1
    plant_type = "flower"    # still hardcoded for Issue 1

    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type)

    print(advice)


main()
