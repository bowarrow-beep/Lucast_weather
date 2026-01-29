from flask import Flask, render_template, request
import pytz
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import requests
from timezonefinder import TimezoneFinder

app = Flask(__name__)

import os
API_KEY = os.getenv("API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    forecast = []

    if request.method == "POST":
        city = request.form["city"]

        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(city)

        tf = TimezoneFinder()
        timezone_name = tf.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(timezone_name)
        local_time = datetime.now(home).strftime("%I:%M %p")

        api_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        json_data = requests.get(api_url).json()

        current = json_data["list"][0]
        weather_data = {
            "city": city,
            "timezone": timezone_name,
            "time": local_time,
            "lat": round(location.latitude, 4),
            "lon": round(location.longitude, 4),
            "temp": current["main"]["temp"],
            "humidity": current["main"]["humidity"],
            "pressure": current["main"]["pressure"],
            "wind": current["wind"]["speed"],
            "desc": current["weather"][0]["description"]
        }

        # 5-day forecast
        for entry in json_data["list"]:
            if "12:00:00" in entry["dt_txt"]:
                forecast.append({
                    "date": entry["dt_txt"].split(" ")[0],
                    "temp": entry["main"]["temp"],
                    "feels": entry["main"]["feels_like"],
                    "icon": entry["weather"][0]["icon"]
                })

    return render_template("index.html", weather=weather_data, forecast=forecast[:5])

if __name__ == "__main__":
    app.run(debug=True)
