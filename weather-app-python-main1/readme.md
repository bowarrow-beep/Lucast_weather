# Weather GUI App

<p>
  <a href="https://www.linkedin.com/in/yashag1" rel="follow opentowork">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="linkedin">
  </a>
</p>

## Introduction
This simple Weather App is a user-friendly application that provides real-time weather data for any city worldwide. The app integrates with the OpenWeather API and features multi-language support for over 50 languages. It offers a sleek, intuitive interface to display key weather metrics such as temperature, wind speed, humidity, and sunrise/sunset times.

## Screenshots
![demo image](https://github.com/user-attachments/assets/2e3547dd-8801-47c6-a6bc-dc55d48e4602)

## Stack Used
- **Language:** Python
- **GUI Framework:** Tkinter
- **API:** OpenWeather API
- **Libraries:** PIL (Pillow), Requests, Dotenv

## How to Run
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simple-weather-app.git
   cd simple-weather-app
2. Install the required packages:
   ```
   pip install -r requirements.txt
3. Run the application:
   ```
   python main.py
## About the Project
The app allows users to search for a city and instantly fetch weather details, such as temperature, wind direction, and humidity. The GUI is designed with simplicity and ease of use in mind. Users can switch between different languages, and the app displays all information in the chosen language.

## Key Features:
- Real-time weather data for any city in the world
- Multi-language support for over 50 languages
- Simple and intuitive Tkinter-based interface
- Custom icons for weather parameters (wind speed, humidity, sunrise, sunset)

## Challenges Faced
1. Certain languages had display issues or were not supported by OpenWeather for some regions. To resolve this, a fallback mechanism is added to handle unsupported language codes gracefully.

2. A method to convert Unix timestamps and calculate the time based on the city’s timezone offset has been implemented.

3. Ensuring proper feedback when the API returned errors (e.g., city not found) is achieved using appropriate message boxes to inform users about invalid inputs or connectivity issues.

## Known Limitations
- Language Compatibility: Not all languages are supported for all regions. Some weather descriptions may appear in English even when a different language is selected.
- Data Accuracy: The app relies entirely on the OpenWeather API. Any inaccuracies or delays from the API can affect the data shown.

## Conclusion
This app combines simplicity with powerful functionality and is a comprehensive solution for users who want a clean, easy-to-use interface for checking weather data in real-time.

## Credits
Icons: <a href="https://www.freepik.com/free-vector/weather-polygonal-icons_3948953.htm#query=weather%20icons%20set&position=2&from_view=keyword&track=ais_hybrid&uuid=4df00539-1723-4082-9948-cdad37d05661">Image by macrovector</a> on Freepik
