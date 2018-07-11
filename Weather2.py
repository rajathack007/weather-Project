import requests
from pprint import pprint
res = requests.get('https://ipinfo.io/')
data = res.json()

location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]
url='http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID=d1a7ed688e1b9155f95106d9a55b9ab0&units=metric'.format(latitude,longitude)
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
