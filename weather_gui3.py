import tkinter as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict

API_KEY = "b7e695f6ea4f0763a17392472fbb111a"

def get_current_weather(city_name):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "lat": data["coord"]["lat"],
            "lon": data["coord"]["lon"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "description": data["weather"][0]["description"].capitalize()
        }
    else:
        return None
    
def get_weather_data(lat, lon):
    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
    url = f"{BASE_URL}lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        daily_temps = defaultdict(list)
        for entry in data["list"]:
            date = entry["dt_txt"].split(" ")[0]
            temp = entry["main"]["temp"]
            daily_temps[date].append(temp)
        averaged_temps = {date: sum(temps) / len(temps) for date, temps in daily_temps.items()}
        return list(averaged_temps.keys()), list(averaged_temps.values())
    else:
        return None, None
    
def fetch_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return
    
    weather_details = get_current_weather(city)
    if not weather_details:
        messagebox.showerror("Error", f"Weather data for '{city}' not found.")
        return
    lat, lon = weather_details["lat"], weather_details["lon"]
    dates, temperatures = get_weather_data(lat, lon)
    if not dates or not temperatures:
        messagebox.showerror("Error", f"5-day forecast for '{city}' not found.")
        return
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dates, temperatures, marker='o', linestyle='-', color='cyan')
    ax.set_title(f"5-Day Temperature Trend for {city.capitalize()}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

root = tk.Tk()
root.title("Weather Application")
root.geometry("800x600")
root.configure(bg="#333333")

input_frame = ttk.Frame(root, padding=10, style="TFrame")
input_frame.pack(side=tk.TOP, fill=tk.X, padx=20)
city_entry = ttk.Entry(input_frame, font=("Arial", 12), width=30)
city_entry.pack(side=tk.LEFT, padx=10)
ttk.Button(input_frame, text="Fetch Data", command=fetch_weather, style="Dark.TButton").pack(side=tk.LEFT, padx=10)
chart_frame = ttk.Frame(root, style="TFrame")
chart_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
root.mainloop()



