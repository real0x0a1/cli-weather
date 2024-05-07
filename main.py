import argparse
import requests

# Set API key from OpenWeatherMap
API_KEY = "YOUR_OPENWEATHER_""

# Set base URL for OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# ASCII art images for different weather conditions
WEATHER_IMAGES = {
    'clear': '☀️',
    'clouds': '☁️',
    'rain': '☔️',
    'thunderstorm': '⛈️',
    'now': '❄️',
    'ist': '💨',
    'fog': '🌫️',
    'haze': '🌫️',
    'dust': '💥',
    'and': '🌴',
    'ash': '🌪️',
    'quall': '💨',
    'tornado': '🌪️',
}

def get_weather_data(city, imperial=False):
    """
    Makes an API request to OpenWeatherMap and returns the weather data as a Python object.

    Args:
        city (str): City name or postal code
        imperial (bool): Whether to use imperial units (default=False)

    Returns:
        dict: Weather information for the specified city
    """
    
    params = {"appid": API_KEY, "q": city}
    if imperial:
        params["units"] = "imperial"
    else:
        params["units"] = "metric"
    response = requests.get(BASE_URL, params=params)
    return response.json()

def print_weather_data(weather_data, imperial=False):
    """
    Prints the weather data in a human-readable format.

    Args:
        weather_data (dict): Weather information for the specified city
        imperial (bool): Whether to use imperial units (default=False)
    """

    weather_condition = weather_data['weather'][0]['main'].lower()
    image = WEATHER_IMAGES.get(weather_condition, '🤔')
    country = weather_data['sys']['country']
    print(f"Weather in {weather_data['name']}, {country}:")
    print(f"  {image} {weather_data['weather'][0]['description']}")
    if imperial:
        print(f"  Temperature: {weather_data['main']['temp']}°F")
    else:
        print(f"  Temperature: {weather_data['main']['temp']}°C")
    print(f"  Humidity: {weather_data['main']['humidity']}%")

def main():
    parser = argparse.ArgumentParser(description="Get the weather")
    parser.add_argument("city", help="City name or postal code")
    parser.add_argument("-f", "--fahrenheit", action="store_true", help="Use Fahrenheit units")
    parser.add_argument("-c", "--celsius", action="store_true", help="Use Celsius units")
    args = parser.parse_args()

    if args.fahrenheit:
        weather_data = get_weather_data(args.city, imperial=True)
        print_weather_data(weather_data, imperial=True)
    elif args.celsius:
        weather_data = get_weather_data(args.city, imperial=False)
        print_weather_data(weather_data, imperial=False)
    else:
        weather_data = get_weather_data(args.city, imperial=False)
        print_weather_data(weather_data, imperial=False)

if __name__ == "__main__":
    main()
