# Gardening advice program with user input, documentation, and improved structure.

# Dictionary storing advice for seasons and plant types
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}


def get_season_advice(season):
    """
    Return gardening advice based on the season.
    If the season is not recognized, return a default message.
    """
    return SEASON_ADVICE.get(season, "No advice for this season.\n")


def get_plant_advice(plant_type):
    """
    Return gardening advice based on the plant type.
    If the plant type is not recognized, return a default message.
    """
    return PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")


def recommend_plants(season):
    """
    Recommend plants based on the season.
    This is a simple example feature.
    """
    recommendations = {
        "summer": "Recommended plants: Sunflowers, Marigolds, Tomatoes.",
        "winter": "Recommended plants: Kale, Spinach, Winter Pansies.",
    }
    return recommendations.get(season, "No plant recommendations available.")


def main():
    """Main program that collects user input and prints gardening advice."""
    
    # Get user input
    season = input("Enter the season (summer/winter): ").lower()
    plant_type = input("Enter the plant type (flower/vegetable): ").lower()

    # Generate advice
    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type)

    # Print advice
    print("\nGardening Advice:")
    print(advice)

    # Optional feature: recommend plants
    print("\nPlant Recommendations:")
    print(recommend_plants(season))


# Run the program
main()
