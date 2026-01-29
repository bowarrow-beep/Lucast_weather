from tkinter import *
from tkinter import Label, messagebox as mb
import requests
from PIL import Image
from datetime import datetime

root = Tk()
root.title("Weather App")
root.configure(bg='lightblue')
root.geometry("700x450")


def get_weather():
    global city_input, temp_field, pressure_field, humidity_field, wind_field
    global cloud_field, sunrise_field, sunset_field, description_field
    city=city_input.get()
    api_key="b7e695f6ea4f0763a17392472fbb111a"
    base_url="http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response=requests.get(base_url.format(city=city, api_key=api_key))
    if response.status_code==200:
        data=response.json()
        main=data['main']
        wind=data['wind']
        sys=data['sys']
        weather=data['weather'][0]

        temp_field.delete(0, END)
        temp_field.insert(0, str(main['temp']*9/5+32)+ " °F")

        pressure_field.delete(0, END)
        pressure_field.insert(0, str(main['pressure']) + " hPa")

        humidity_field.delete(0, END)
        humidity_field.insert(0, str(main['humidity']) + " %")

        wind_field.delete(0, END)
        wind_field.insert(0, str(wind['speed']) + " m/s")

        cloud_field.delete(0, END)
        cloud_field.insert(0, str(data['clouds']['all']) + " %")

        sunrise_time = datetime.fromtimestamp(sys['sunrise']).strftime('%H:%M:%S')
        sunset_time = datetime.fromtimestamp(sys['sunset']).strftime('%H:%M:%S')

        sunrise_field.delete(0, END)
        sunrise_field.insert(0, sunrise_time)

        sunset_field.delete(0, END)
        sunset_field.insert(0, sunset_time)

        description_field.delete(0, END)
        description_field.insert(0, weather['description'])
    else:
        mb.showerror("City Not Found")
        city_input.delete(0, END)

def reset():
    city_input.delete(0, END)
    temp_field.delete(0, END)
    pressure_field.delete(0, END)
    humidity_field.delete(0, END)
    wind_field.delete(0, END)
    cloud_field.delete(0, END)
    sunrise_field.delete(0, END)
    sunset_field.delete(0, END)
    description_field.delete(0, END)
def get_forecast():
    url1=  'https://wttr.in/{}.png?m'.format(city_input.get())
    response1=requests.get(url1)
    path='forecast_weather.png'
    if response1.status_code==200:
        with open('forecast_weather.png', 'wb') as f:
            f.write(response1.content)
        img=Image.open('forecast_weather.png')
        img.show()

title=Label(root, text="Weather detection and forecast", font=("bold", 20), bg='lightblue')
label1=Label(root, text="Enter City Name:", font=("bold", 12), bg='lightblue')
city_input =Entry(root, width=24, fg= 'red2', font=12, relief=GROOVE)
timelabel= Label(root, font=("bold", 14), bg='lightblue')

btn_submit= Button(root, text="Search city", width=12, bg='blue', fg='white', font=("bold", 12), command=get_weather)
btn_forecast= Button(root, text="Forecast", width=12, bg='blue', fg='white', font=("bold", 12), command=get_forecast)
btn_reset= Button(root, text="Reset ", width=12, bg='blue', fg='white', font=("bold", 12) , command=reset)

label2=Label(root, text=" Temperature", font=("bold", 12), bg='lightblue', justify=LEFT)
label3=Label(root, text="Pressure", font=("bold", 12), bg='lightblue', justify=LEFT)
label4=Label(root, text="Humidity", font=("bold", 12), bg='lightblue', justify=LEFT)
label5=Label(root, text="Wind", font=("bold", 12), bg='lightblue', justify=LEFT)
label6=Label(root, text="Cloudiness", font=("bold", 12), bg='lightblue', justify=LEFT)
label7=Label(root, text="Sunrise", font=("bold", 12), bg='lightblue', justify=LEFT)
label8=Label(root, text="Sunset", font=("bold", 12), bg='lightblue', justify=LEFT)
label9=Label(root, text="Description", font=("bold", 12), bg='lightblue', justify=LEFT)

temp_field=Entry(root, width=24, fg='red2', font=11, relief=GROOVE)
pressure_field=Entry(root, width=24, fg='red2', font=11, relief=GROOVE)
humidity_field=Entry(root, width=24, fg='red2', font=11, relief=GROOVE)
wind_field=Entry(root, width=24, fg='red2', font=11, relief=GROOVE)
cloud_field=Entry(root, width=24, fg='red2', font=11, relief=GROOVE)
sunrise_field=Entry(root, width=24, fg='red2', font=11, relief=GROOVE)
sunset_field=Entry(root, width=24, fg='red2', font=11, relief=GROOVE)
description_field=Entry(root, width=24, fg='red2', font=11, relief=GROOVE)
btn_submit.grid(row=2, column=0, pady=5)
btn_forecast.grid(row=2, column=1, pady=5)
label2.grid(row=3, column=0, pady=5, sticky=W)
label3.grid(row=4, column=0, pady=5, sticky=W)
label4.grid(row=5, column=0, pady=5, sticky=W)
label5.grid(row=6, column=0, pady=5, sticky=W)
label6.grid(row=7, column=0, pady=5, sticky=W)
label7.grid(row=8, column=0, pady=5, sticky=W)
label8.grid(row=9, column=0, pady=5, sticky=W)
label9.grid(row=10, column=0, pady=5, sticky=W)

city_input.grid(row=1, column=1, padx=5)
temp_field.grid(row=3, column=1, pady=5)
pressure_field.grid(row=4, column=1, pady=5)
humidity_field.grid(row=5, column=1, pady=5)
wind_field.grid(row=6, column=1, pady=5)
cloud_field.grid(row=7, column=1, pady=5)
sunrise_field.grid(row=8, column=1, pady=5)
sunset_field.grid(row=9, column=1, pady=5)
description_field.grid(row=10, column=1, pady=5)
btn_reset.grid(row=11, column=1, pady=5)

root.mainloop()