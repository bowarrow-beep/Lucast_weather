import tkinter as tk
from tkinter import ttk
from weather_data import get_weather
from icon_loader import load_icon
from lang_code import lang_code_table

# Initialize the tkinter window
root = tk.Tk()
root.title("Weather App")

# Set up the city input field and button
city_entry = tk.Entry(root, font=("Arial", 14), width=13)
city_entry.grid(row=0, column=0, padx=10, pady=10)

def fetch_weather():
    get_weather(city_entry, language_var, temp_label, desc_label, city_label, windspeed_label, humidity_label, sunrise_label, sunset_label)

search_button = tk.Button(root, text="Get weather", font=("Arial", 14), command=fetch_weather)
search_button.grid(row=0, column=1, padx=10, pady=10)

# Language selection menu
language_var = tk.StringVar(value='English')  # Default language
language_label = tk.Label(root, text="Select Language:", font=("Arial", 13))
language_label.grid(row=1, column=0, padx=10, pady=(0, 15))

language_menu = ttk.Combobox(
    root, textvariable=language_var, state='readonly', width=14,
    values=[ lang for lang in lang_code_table.keys() ],
    font=("Arial", 13)
)
language_menu.grid(row=1, column=1, padx=10, pady=(0, 15))
language_menu.config(height=5)

# Weather Labels
temp_label = tk.Label(root, text="", font=("Arial", 40))
temp_label.grid(row=2, column=0, columnspan=2)

city_label = tk.Label(root, text="", font=("Arial", 16))
city_label.grid(row=3, column=0, columnspan=2)

desc_label = tk.Label(root, text="", font=("Arial", 16))
desc_label.grid(row=4, column=0, columnspan=2, pady=(0, 10))

# Icons and values
icon1 = load_icon("icons/icon1.png")
icon2 = load_icon("icons/icon2.png")
icon3 = load_icon("icons/icon3.png")
icon4 = load_icon("icons/icon4.png")

icon1_label = tk.Label(root, image=icon1)
icon1_label.grid(row=5, column=0, padx=10, pady=10)
windspeed_label = tk.Label(root, text="Wind", font=("Arial", 16))
windspeed_label.grid(row=6, column=0)

icon2_label = tk.Label(root, image=icon2)
icon2_label.grid(row=5, column=1, padx=10, pady=10)
humidity_label = tk.Label(root, text="Humidity", font=("Arial", 16))
humidity_label.grid(row=6, column=1)

icon3_label = tk.Label(root, image=icon3)
icon3_label.grid(row=7, column=0, padx=10, pady=10)
sunrise_label = tk.Label(root, text="Sunrise", font=("Arial", 16))
sunrise_label.grid(row=8, column=0)

icon4_label = tk.Label(root, image=icon4)
icon4_label.grid(row=7, column=1, padx=10, pady=10)
sunset_label = tk.Label(root, text="Sunset", font=("Arial", 16))
sunset_label.grid(row=8, column=1)

# Additional Info
info_label = tk.Label(root, text=(
    "Forecasted data is in the city's timezone.\n"
    "Some languages may not work for some other regions.\n"
    "Created by Yash Agarwal"
), font=("Arial", 12))
info_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter loop
root.mainloop()
