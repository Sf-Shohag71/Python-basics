def location(city, country, population=0):
    """Find out city and country location"""
    if population:
        user_location = f"{city} {country} - {population}"
    else:
        user_location = f"{city} {country}"
    return user_location.title()