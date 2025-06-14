import requests
from modules.tts_engine import speak
import os
from dotenv import load_dotenv

open_weather_api_key=os.getenv("open_weathermap_api_key")

def get_weather(city):
  api_key=open_weather_api_key
  base_url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
  res=requests.get(base_url).json()
  if res.get("main"):
    temp=res['main']['temp']
    description=res['weather'][0]['description']
    speak(f"Temperature in {city} is {temp} °C with {description}")
  else:
    speak("Couldn't fetch weather details")
    