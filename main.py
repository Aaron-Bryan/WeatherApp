import requests
import json

from tkinter import *
from datetime import datetime

#Initialize tkinter window
root = Tk()
root.geometry("400x400")
root.resizable(0, 0)

root.title("Weather App")

loc_value = StringVar()

text_field = Text(root, width=46, height=10)

#Main Function
def show_weather():
    #API Key
    api_key = "aa4b0f367f2eabc64faf46c61849b120"

    #Get location from user from the input_loc variable
    loc_name = loc_value.get()

    #URL of the API
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + loc_name + '&appid='+ api_key

    #Get the response from the URL
    response = requests.get(api_url)

    #Covert the response from json to a readable python format.
    weather_info = response.json()

    #Clearing the text field for new outputs
    text_field.delete("1.0", "end")

    #cod = 200 -> Means weather data is successfully fetched
    if weather_info["cod"] == 200:

        #Get the values from the weather values from the weather_info variable.

        # From kelvin to celsius (C = K - 273.15)
        temperature = int(weather_info["main"]["temp"] - 273)

        pressure = weather_info["main"]["pressure"]
        humidity = weather_info["main"]["humidity"]
        wind_speed = weather_info["wind"]["speed"]

        estimated_sunrise = weather_info["sys"]["sunrise"]
        estimated_sunset = weather_info["sys"]["sunset"]

        #sunrise_time =
        #sunset_time =

        timezone = weather_info["timezone"]

        cloud_density = weather_info["clouds"]["all"]

        weather_description = weather_info["weather"][0]["description"]

        #Assign the values in this string format.

        """weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
        else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!""""

        weather_summary = f"{location_name}\n Temperature: {temperature} °C \n Pressure: {pressure} hPA \n Humidity: {humidity} \n Estimated Sunrise time: {estimated_sunrise} \n Estimated Sunset time {estimated_sunset} \n Cloud Density: {cloud_density}\n Desc.: {weather_description}"

    else:
        weather_summary = f"Weather for {location_name} not found."