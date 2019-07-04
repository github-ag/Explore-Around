import pandas as pd
import numpy as np
from spellchecker import SpellChecker
spell = SpellChecker()
df = pd.read_csv('worldcities.csv')
list_of_cities = np.array(df['city'])
list_of_countries = np.array(df['country'])
import requests
def weather(city):
    url = 'https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'.format(city)
    res = requests.get(url)
    # print(res)
    data = res.json()
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    des = data['weather'][0]['description']
    print('Temperature :', temp, )
    print('Wind Speed :', wind_speed, 'm/s')
    print('Latitude :', latitude)
    print('Longitude :', longitude)
    print('Description : ', des)

city = input("Enter your city ")
word = spell.correction(city)
word = word.capitalize() # capitalize the first alphabet
#print(word)
if word==city:
    weather(city)
else:
    if word in list_of_cities or word in list_of_countries:
        print('Did you mean : ',word)
        ch=input()
        if ch=='y':
            weather(word)
        else:
            print('Enter correct city')
    else:
        print('Enter correct city')








