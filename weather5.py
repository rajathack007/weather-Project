import requests
from pprint import pprint
import tkinter
from tkinter import *
root=Tk()
root.geometry("350x90")
root.title("Sunshine")
img = PhotoImage(file='weather.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.resizable(False,False)
def show():
    root.geometry("350x500")
    x=(entry_city.get())
    print(x)
    url='http://api.openweathermap.org/data/2.5/weather?q={}&APPID=d1a7ed688e1b9155f95106d9a55b9ab0&units=metric'.format(x)
    res=requests.get(url)
    data=res.json()
    temp=data['main']['temp']
    wind_speed=data['wind']['speed']
    latitude=data['coord']['lat']
    longitude=data['coord']['lon']
    description=data['weather'][0]['description']
    pprint(data)
    print('Temperature:{} degree celcius'.format(temp))
    print('wind speed:{}m/s'.format(wind_speed))
    print('Latitude:{}'.format(latitude))
    print('Longitude:{}'.format(longitude))
    print('Description:{}'.format(description))
    city.config(text=x)
    l.config(text=temp)
    l1.config(text=wind_speed)
    l2.config(text=latitude)
    l3.config(text=longitude)
    l4.config(text=description)


label_city=Label(root,text="City",width=10,font=90)
label_city.grid(row=0,columnspan=2,pady=6)
entry_city=Entry(root,width=30)
entry_city.grid(row=0,column=3)
b=Button(root,text="Show Weather",width=15,bg='red',fg='black',command=show)
b.grid(row=1,column=3)
city=Label(root,text="")
city.grid(row=2,column=3,pady=4)
temp=Label(root,text="Temperature  :-")
temp.grid(row=3,column=0)
l=Label(root,text="")
l.grid(row=3,column=1)
wind=Label(root,text="Wind Speed  :-")
wind.grid(row=4,column=0)
l1=Label(root,text="")
l1.grid(row=4,column=1)
latitude=Label(root,text="Latitude  :-")
latitude.grid(row=5,column=0)
l2=Label(root,text="")
l2.grid(row=5,column=1)
longitude=Label(root,text="Longitude  :-")
longitude.grid(row=6,column=0)
l3=Label(root,text="")
l3.grid(row=6,column=1)
description=Label(root,text="Description  :-")
description.grid(row=7,column=0)
l4=Label(root,text="")
l4.grid(row=7,column=1)


root.mainloop()
