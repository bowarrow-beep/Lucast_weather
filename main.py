from tkinter import *
import tkinter as tk
import pytz
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import requests
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
from timezonefinder import TimezoneFinder


root=Tk()
root.title("Lucast Weather")
root.geometry("750x470+300+200")
root.resizable(False, False)
root.config(bg="#0049a2")



def getWeather():
    city=textfield.get()
    geolocator=Nominatim(user_agent="new")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)

    long_lat.config(text=f"{round(location.latitude,4)}°N | {round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    apikey="b7e695f6ea4f0763a17392472fbb111a"
    api=f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"

    json_data=requests.get(api).json()
    print(json_data)

    #current weather from first forcast entry
    current = json_data['list'][0]
    temp=current['main']['temp']
    humidity=current['main']['humidity']
    pressure=current['main']['pressure']
    wind_speed=current['wind']['speed']
    description=current['weather'][0]['description']

    t.config(text=f"{temp}°C")
    h.config(text=f"{humidity}%")
    p.config(text=f"{pressure} hPa")
    w.config(text=f"{wind_speed} m/s")
    d.config(text=f"{description}")

    #Daily forecast
    daily_data = []
    for entry in json_data['list']:
        if '12:00:00' in entry['dt_txt']:
            daily_data.append(entry)
    
    icons = []
    temps = []

    for i in range(5):
        if i > len(daily_data):
            break
        icon_code = daily_data[i]['weather'][0]['icon']
        img=Image.open(f"icon/{icon_code}@2x.png").resize((50,50))
        icons.append(ImageTk.PhotoImage(img))
        temps.append((daily_data[i]['main']['temp'],daily_data[i]['main']['feels_like']))

    day_widget = [
        (firstimage,day1,day1temp),
        (secondimage,day2,day2temp),
        (thirdimage,day3,day3temp),
        (fourthimage,day4,day4temp),
        (fifthimage,day5,day5temp)
    ]
        
    for i,(img_label,day_label,temp_label) in enumerate(day_widget):
        if i >= len(icons):
            break
        img_label.config(image=icons[i])
        img_label.image=icons[i]
        temp_label.config(text=f"Temp: {round(temps[i][0],1)}°C\nFeel: {round(temps[i][1],1)}°C")
        future_date = datetime.now() + timedelta(days=i)
        day_label.config(text=future_date.strftime("%A"))



##icon
image_icon=PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)
Round_box=PhotoImage(file="Images/Rounded rectangle 1.png")
Label(root,image=Round_box,bg="#0049a2").place(x=30,y=60)




#label
label1=Label(root,text="Temperature:",font=("arial",10),bg="#aad1c8",fg="#323661")
label1.place(x=40,y=120)

label2=Label(root,text="Humidity:",font=("arial",10),bg="#aad1c8",fg="#323661")
label2.place(x=40,y=140)

label3=Label(root,text="Pressure:",font=("arial",10),bg="#aad1c8",fg="#323661")
label3.place(x=40,y=160)

label4=Label(root,text="Wind speed:",font=("arial",10),bg="#aad1c8",fg="#323661")
label4.place(x=40,y=180)

label5=Label(root,text="Description:",font=("arial",10),bg="#aad1c8",fg="#323661")
label5.place(x=40,y=200)



#Search  box

Search_image=PhotoImage(file="Images/Rounded rectangle 3.png")
myimage=Label(root,image=Search_image,bg="#0049a2")
myimage.place(x=270,y=122)  

weat_image=PhotoImage(file="Images/layer 7.png")
weatherimage=Label(root,image=weat_image,bg="#333c4c")
weatherimage.place(x=290,y=127)

textfield=Entry(root,justify="center",width=15,font=("poppins",25,"bold"),bg="#333c4c",border=0,fg="white")
textfield.place(x=370,y=130)


Search_icon=PhotoImage(file="Images/layer 6.png")
myimage_icon=Button(root,image=Search_icon,borderwidth=0,cursor="hand2",bg="#333c4c", command=getWeather)
myimage_icon.place(x=640,y=135)


#Bottom box
frame=Frame(root,width=900,height=180,bg="#7094d4")
frame.pack(side=BOTTOM)

#boxes
firstbox=PhotoImage(file="Images/Rounded rectangle 2.png")
secondbox=PhotoImage(file="Images/Rounded rectangle 2 copy.png")

Label(frame,image=firstbox,bg="#7094d4").place(x=30,y=20)
Label(frame,image=secondbox,bg="#7094d4").place(x=300,y=30)
Label(frame,image=secondbox,bg="#7094d4").place(x=400,y=30)
Label(frame,image=secondbox,bg="#7094d4").place(x=500,y=30)
Label(frame,image=secondbox,bg="#7094d4").place(x=600,y=30)


#clock
clock=Label(root,text="Lucast Weather",font=("Helvetica",20),bg="#0049a2",fg="white")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=("Helvetica",20),bg="#0049a2",fg="white")
timezone.place(x=275,y=20)

long_lat=Label(root,font=("Helvetica",10),bg="#0049a2",fg="white")
long_lat.place(x=275,y=50)


#thpwd
t=Label(root,font=("Helvetica",9),bg="#aad1c8",fg="#333c4c")
t.place(x=120,y=120)

h=Label(root,font=("Helvetica",9),bg="#aad1c8",fg="#333c4c")
h.place(x=120,y=140)

p=Label(root,font=("Helvetica",9),bg="#aad1c8",fg="#333c4c")
p.place(x=120,y=160)

w=Label(root,font=("Helvetica",9),bg="#aad1c8",fg="#333c4c")
w.place(x=120,y=180)

d=Label(root,font=("Helvetica",9),bg="#aad1c8",fg="#333c4c")
d.place(x=120,y=200)

#first cell
firstframe=Frame(root,width=230,height=132,bg="#333c4c")
firstframe.place(x=35,y=315)

firstimage=Label(firstframe,bg="#333c4c")
firstimage.place(x=1,y=15)

day1=Label(firstframe,font=("arial",20),bg="#333c4c",fg="white")
day1.place(x=100,y=5)

day1temp=Label(firstframe,font=("arial",15),bg="#333c4c",fg="white")
day1temp.place(x=100,y=50)

#second cell
secondframe=Frame(root,width=70,height=115,bg="#eeefea")
secondframe.place(x=305,y=325)

secondimage=Label(secondframe,bg="#eeefea" ,anchor="center")
secondimage.place(x=7,y=20)

day2=Label(secondframe,font=("arial",8),bg="#eeefea",fg="#000",anchor="center")
day2.place(x=10,y=5)

day2temp=Label(secondframe,font=("arial",8),bg="#eeefea",fg="#000",anchor="center")
day2temp.place(x=2,y=70)

#third cell
thirdframe=Frame(root,width=70,height=115,bg="#eeefea")
thirdframe.place(x=405,y=325)

thirdimage=Label(thirdframe,bg="#eeefea",anchor="center")
thirdimage.place(x=7,y=20)

day3=Label(thirdframe,font=("arial",8),bg="#eeefea",fg="#000",anchor="center")
day3.place(x=10,y=5)

day3temp=Label(thirdframe,font=("arial",8),bg="#eeefea",fg="#000",anchor="center")
day3temp.place(x=2,y=70)

#fourth cell
fourthframe=Frame(root,width=70,height=115,bg="#eeefea")
fourthframe.place(x=505,y=325)

fourthimage=Label(fourthframe,bg="#eeefea",anchor="center")
fourthimage.place(x=7,y=20)

day4=Label(fourthframe,font=("arial",8),bg="#eeefea",fg="#000",anchor="center")
day4.place(x=10,y=5)

day4temp=Label(fourthframe,font=("arial",8),bg="#eeefea",fg="#000",anchor="center")
day4temp.place(x=2,y=70)

#fifth cell
fifthframe=Frame(root,width=70,height=115,bg="#eeefea")
fifthframe.place(x=605,y=325)

fifthimage=Label(fifthframe,bg="#eeefea",anchor="center")
fifthimage.place(x=7,y=20)

day5=Label(fifthframe,font=("arial",8),bg="#eeefea",fg="#000",anchor="center")
day5.place(x=10,y=5)

day5temp=Label(fifthframe,font=("arial",8),bg="#eeefea",fg="#000",anchor="center")
day5temp.place(x=2,y=70)


root.mainloop()

