from tkinter import *

import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import requests
import pytz
root=Tk()
root.title("Weather App")
root.geometry("890x325+310+200")
root.config(bg="#57adff")
root.resizable(False,False)
root.iconbitmap('C:/Users/Lenovo/Desktop/weather project/images/apple.ico')


def getWeather():
    
        city=textfield.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj=TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        timezone.config(text=result)
        long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")
        



        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
       

        # api="https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=f0b8a18836205329b113f9c00d0a611d"
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c36518e57990c185e0963054b623dc37"

        json_data = requests.get(api).json()
       
        description = json_data["weather"][0]["description"]
        temp= int(json_data["main"]["temp"] - 273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind= json_data["wind"]["speed"]

     
        t.config(text=(temp,"°C"))
        h.config(text=(humidity,"%"))  
        w.config(text=(wind,"m/s"))
        p.config(text=(pressure,"hPa"))
        d.config(text=description)
       

Round_box=PhotoImage(file="images/Rounded Rectangle 1.png")
Label(root,image=Round_box, bg="#57adff").place(x=40,y=110)

#label
label1=Label(root,text="Temperature", font=("Helvetica",12),fg="white",bg="#203243")
label1.place(x=50,y=120)

label2=Label(root,text="Humidity", font=("Helvetica",12),fg="white",bg="#203243")
label2.place(x=50,y=140)

label3=Label(root,text="Pressure", font=("Helvetica",12),fg="white",bg="#203243")
label3.place(x=50,y=160)

label4=Label(root,text="Wind", font=("Helvetica",12),fg="white",bg="#203243")
label4.place(x=50,y=180)

label5=Label(root,text="Description", font=("Helvetica",12),fg="white",bg="#203243")
label5.place(x=50,y=200)

Search_image=PhotoImage(file="C:/Users/Lenovo/Desktop/weather project/images/Rounded Rectangle 3.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=270 , y=140)

weat_image=PhotoImage(file="C:/Users/Lenovo/Desktop/weather project/images/Layer 7.png")
weatherimage=Label(image=weat_image,bg="#203243")
weatherimage.place(x=290,y=145)

weat_image2=PhotoImage(file="C:/Users/Lenovo/Desktop/weather project/images/ICON1.png")
weatherimage=Label(image=weat_image2,bg="#57adff")
weatherimage.place(x=400,y=0)

textfield=tk.Entry(root,justify="center",width=15,font=("poppins",25,"bold"),bg="#203243",border=0,fg="white")
textfield.place(x=370, y=145)
textfield.focus()

Search_icon=PhotoImage(file="C:/Users/Lenovo/Desktop/weather project/images/Layer 6.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=145)


clock=Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=50,y=30)

timezone=Label(root,font=("Helvetica",20,'bold'),fg="white",bg="#57adff")
timezone.place(x=650,y=10)

long_lat=Label(root,font=("Helvetica",15,),fg="white",bg="#57adff")
long_lat.place(x=650,y=50)

t=Label(root,font=("Helvetica",12),fg="white",bg="#203243")
t.place(x=150,y=120)

h=Label(root,font=("Helvetica",12),fg="white",bg="#203243")
h.place(x=150,y=140)

p=Label(root,font=("Helvetica",12),fg="white",bg="#203243")
p.place(x=150,y=160)

w=Label(root,font=("Helvetica",12),fg="white",bg="#203243")
w.place(x=150,y=180)

d=Label(root,font=("Helvetica",12),fg="white",bg="#203243")
d.place(x=150,y=200)

root.mainloop()