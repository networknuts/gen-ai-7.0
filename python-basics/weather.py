import requests
from dotenv import load_dotenv
import os

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
COUNTRY_CODE = input("Enter your country code: ")
ZIP_CODE = input("Enter your zip code: ")

weather_url = f"https://api.openweathermap.org/data/2.5/weather?zip={ZIP_CODE},{COUNTRY_CODE}&appid={WEATHER_API_KEY}"

response = requests.get(weather_url)

if response.status_code == 200:
    print(response.json())
else:
    print("Error: something went wrong.")