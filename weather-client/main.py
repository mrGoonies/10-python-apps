import collections
import requests

Local = collections.namedtuple("Local", "city country")
Weather = collections.namedtuple("Weather", "location units temp condition")


def assign_json_values_to_tuple(json_response: dict) -> None:
    """Assign the values from the json response to the Weather tuple

    :param json_response: dict of the json response
    :return: None
    """

    weather = Weather(
        location=json_response.get("location").get("city"),
        units=json_response.get("units"),
        temp=json_response.get("forecast").get("temp"),
        condition=json_response.get("weather").get("description")
    )

    print(f"The weather in {weather.location} is {weather.temp} degrees and {weather.condition}")


def get_weather(locations_text: str) -> dict:
    city = locations_text.split(",")[0]
    country = locations_text.split(",")[1].strip()

    url = f"https://weather.talkpython.fm/api/weather?city={city}&country={country}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
    else:
        print(response.json())

        return response.json()


def validate_inputs(city: str, country: str) -> tuple:
    """Validate the inputs from the user

    :param city: string of the city
    :param country: Tuple of the city and country
    :return: tuple of strings (country, city)
    """

    if city == "" or country == "":
        print("You must enter a city and country\nPlease try again!\n")
        return get_location_user()

    else:
        print(f"You selected {city}, {country}")

        return Local(city, country)


def get_location_user():
    """Get the location from the user

    :return: tuple of strings (country, city)
    """

    user_city = input("Enter your city: \n>>> ")
    user_country = input("Enter your country: \n>>> ")

    return validate_inputs(user_city.title(), user_country.upper())


def convert_plaintext_location(location_text: collections.namedtuple) -> str:
    """Convert the location tuple into a string

    :param location_text: tuple of strings (country, city)
    :return: string of location in the format "city, country"
    """

    location_text: str = f"{location_text.city}, {location_text.country}"
    return location_text


if __name__ == '__main__':
    print("-" * 30)
    print("\t\t\tWeather Client App")
    print("-" * 30)
    location = convert_plaintext_location(get_location_user())
    #get_weather(location)
    assign_json_values_to_tuple(get_weather(location))
