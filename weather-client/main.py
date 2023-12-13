def validate_inputs(city: str, country: str):
    """Validate the inputs from the user

    :param city: string of the city
    :param country: Tuple of the city and country"""

    if city == "" or country == "":
        print("You must enter a city and country\nPlease try again!\n")
        return get_location_user()

    else:
        print(f"You selected {city}, {country}")
        return country, city


def get_location_user():
    """Get the location from the user

    :return: tuple of strings (country, city)
    """

    user_city = input("Enter your city: \n>>> ")
    user_country = input("Enter your country: \n>>> ")

    return validate_inputs(user_city.title(), user_country.upper())


def convert_plaintext_location(location_text: tuple) -> str:
    """Convert the location tuple into a string

    :param location_text: tuple of strings (country, city)
    :return: string of location in the format "city, country"
    """

    location_text = f"{location_text[0]}, {location_text[1]}"
    return location_text


if __name__ == '__main__':
    print("-" * 30)
    print("\t\t\tWeather Client App")
    print("-" * 30)
    convert_plaintext_location(get_location_user())
