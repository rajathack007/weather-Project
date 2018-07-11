import requests
from pprint import pprint
import tkinter
from tkinter import *
import datetime
from datetime import date
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
    temp=str(data['main']['temp'])+' degree celcius'
    wind_speed=str(data['wind']['speed'])+' m/s'
    latitude=data['coord']['lat']
    longitude=data['coord']['lon']
    description=data['weather'][0]['description']
    pressure=str(data['main']['pressure'])+' hPa'
    temp_max=str(data['main']['temp_max'])+' degree celsius'
    temp_min=str(data['main']['temp_max'])+' degree celsius'
    humidity=str(data['main']['humidity'])+' %'
    country=data['sys']['country']
    wind_direction=str(data['wind']['deg'])+' degree'
    pprint(data)
    print('Temperature:{} '.format(temp))
    print('wind speed:{}'.format(wind_speed))
    print('Latitude:{}'.format(latitude))
    print('Longitude:{}'.format(longitude))
    print('Description:{}'.format(description))
    print('Pressure:{}'.format(pressure))
    print('Temperature max:{} '.format(temp_max))
    print('Temperature min:{} '.format(temp_min))
    print('Humidity:{}'.format(humidity))
    print('Country:{}'.format(country))
    print('Wind Direction:{}'.format(wind_direction))

    current_date = datetime.date.today()
    print(current_date)


    date.config(text=current_date)
    city.config(text=x)
    l.config(text=temp)
    l1.config(text=wind_speed)
    l2.config(text=latitude)
    l3.config(text=longitude)
    l4.config(text=description)
    l5.config(text=pressure)
    l6.config(text=temp_max)
    l7.config(text=temp_min)
    l8.config(text=humidity)
    l9.config(text=country)
    l10.config(text=wind_direction)



label_city=Label(root,text="City",width=10,font=90)
label_city.grid(row=0,column=0,pady=6)
entry_city=Entry(root,width=30)
entry_city.grid(row=0,column=1)
b=Button(root,text="Show Weather",width=15,bg='red',fg='black',command=show)
b.grid(row=1,column=1)
city=Label(root,text="",font=20)
city.grid(row=2,column=1,pady=4)
date=Label(root,text="",font=20)
date.grid(row=3,column=1,pady=4)
temp=Label(root,text="Temperature  :-")
temp.grid(row=4,column=0)
l=Label(root,text="")
l.grid(row=4,column=1)
wind=Label(root,text="Wind Speed  :-")
wind.grid(row=5,column=0)
l1=Label(root,text="")
l1.grid(row=5,column=1)
latitude=Label(root,text="Latitude  :-")
latitude.grid(row=6,column=0)
l2=Label(root,text="")
l2.grid(row=6,column=1)
longitude=Label(root,text="Longitude  :-")
longitude.grid(row=7,column=0)
l3=Label(root,text="")
l3.grid(row=7,column=1)
description=Label(root,text="Description  :-")
description.grid(row=8,column=0)
l4=Label(root,text="")
l4.grid(row=8,column=1)
pressure=Label(root,text="Pressure :-")
pressure.grid(row=9,column=0)
l5=Label(root,text="")
l5.grid(row=9,column=1)
temp_max=Label(root,text="Temperature Max :-")
temp_max.grid(row=10,column=0)
l6=Label(root,text="")
l6.grid(row=10,column=1)
temp_min=Label(root,text="Temperature Min :-")
temp_min.grid(row=11,column=0)
l7=Label(root,text="")
l7.grid(row=11,column=1)
humidity=Label(root,text="Humidity :-")
humidity.grid(row=12,column=0)
l8=Label(root,text="")
l8.grid(row=12,column=1)
country=Label(root,text="Country :-")
country.grid(row=13,column=0)
l9=Label(root,text="")
l9.grid(row=13,column=1)
wind_direction=Label(root,text="Wind Direction :-")
wind_direction.grid(row=14,column=0)
l10=Label(root,text="")
l10.grid(row=14,column=1)


root.mainloop()
