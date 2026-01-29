import tkinter as tk
from tkinter import messagebox
import requests
class WeatherForecast:
   def __init__(self, root):
       self.root = root
       self.root.title("Weather Forecast")
       self.root.geometry("400x300")
       # City Input
       tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
       self.city_entry = tk.Entry(root, font=("Arial", 12))
       self.city_entry.pack(pady=5)
       # Search Button
       tk.Button(root, text="Get Weather", command=self.get_weather, font=("Arial", 12)).pack(pady=10)
       # Result Labels
       self.result_label = tk.Label(root, text="", font=("Arial", 12))
       self.result_label.pack(pady=10)
   def get_weather(self):
       city = self.city_entry.get()
       if not city:
           messagebox.showerror("Error", "City name cannot be empty!")
           return
       api_key = "b7e695f6ea4f0763a17392472fbb111a" # Replace with your API key
       url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
       try:
           response = requests.get(url)
           data = response.json()
           if data["cod"] != 200:
               messagebox.showerror("Error", data["message"])
               return
           temp_celsius = data["main"]["temp"]
           temp_fahrenheit = (temp_celsius * 9/5) + 32
           weather_desc = data["weather"][0]["description"]
           result_text = (
               f"City: {city}\n"
               f"Temperature: {temp_celsius:.2f}°C / {temp_fahrenheit:.2f}°F\n"
               f"Weather: {weather_desc.capitalize()}"
           )
           self.result_label.config(text=result_text)
       except Exception as e:
           messagebox.showerror("Error", f"Failed to fetch weather data: {e}")
# Main Function
if __name__ == "__main__":
   root = tk.Tk()
   app = WeatherForecast(root)
   root.mainloop()