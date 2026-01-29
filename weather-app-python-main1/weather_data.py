import requests
from tkinter import messagebox
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv
from lang_code import lang_code_table

load_dotenv()
api_key = "b7e695f6ea4f0763a17392472fbb111a"

def get_weather(city_entry, language_var, temp_label, desc_label, city_label, windspeed_label, humidity_label, sunrise_label, sunset_label):
    city = city_entry.get()
    lang = language_var.get()
    lang_code = lang_code_table.get(lang, "en")
    if city:
        base_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang={}'.format(city, api_key, lang_code)
        response = requests.get(base_url)
        data = response.json()

        if data['cod'] == 200:
            temperature = data['main']['temp']
            windspeed = data['wind']['speed']
            winddegree = data['wind']['deg']
            humidity = data['main']['humidity']
            weather_desc = data['weather'][0]['description']
            city_name = data['name']
            country = data['sys']['country']
            timezone_offset = data['timezone']

            temp_label.config(text=f'{temperature}°C')
            desc_label.config(text=weather_desc.capitalize())
            city_label.config(text=f'{city_name}, {country}')
            windspeed_label.config(text=f'{windspeed} m/s from {get_wind_direction(winddegree)}')
            humidity_label.config(text=f'{humidity}%')
            sunrise_label.config(text=convert_unix_to_local(data['sys']['sunrise'], timezone_offset))
            sunset_label.config(text=convert_unix_to_local(data['sys']['sunset'], timezone_offset))
        else:
            messagebox.showerror("Error", "City not found!")
    else:
        messagebox.showerror("Error", "Please enter a city name!")

def get_wind_direction(degrees):
    if degrees >= 348.75 or degrees < 11.25:
        return 'N'
    
    directions = [
        (11.25, 33.75, 'NNE'), (33.75, 56.25, 'NE'), (56.25, 78.75, 'ENE'), (78.75, 101.25, 'E'), 
        (101.25, 123.75, 'ESE'), (123.75, 146.25, 'SE'), (146.25, 168.75, 'SSE'), (168.75, 191.25, 'S'), 
        (191.25, 213.75, 'SSW'), (213.75, 236.25, 'SW'), (236.25, 258.75, 'WSW'), (258.75, 281.25, 'W'), 
        (281.25, 303.75, 'WNW'), (303.75, 326.25, 'NW'), (326.25, 348.75, 'NNW')
    ]

    for start, end, direction in directions:
        if start <= degrees < end:
            return direction

def convert_unix_to_local(unix_timestamp, timezone_offset_seconds):
    utc_time = datetime.utcfromtimestamp(unix_timestamp).replace(tzinfo=timezone.utc)
    local_timezone = timezone(timedelta(seconds=timezone_offset_seconds))
    local_time = utc_time.astimezone(local_timezone)
    return local_time.strftime('%H:%M')
