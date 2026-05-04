import requests

WEATHER_API_KEY = #enter your key
COUNTRY_CODE = input("Enter your country code: ")
ZIP_CODE = input("Enter your zip code: ")

weather_url = f"https://api.openweathermap.org/data/2.5/weather?zip={ZIP_CODE},{COUNTRY_CODE}&appid={WEATHER_API_KEY}"

response = requests.get(weather_url)
print(response.json())