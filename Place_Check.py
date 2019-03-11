import pandas as pd
import numpy as np
from spellchecker import SpellChecker
spell = SpellChecker()
df = pd.read_csv('worldcities.csv')
list_of_cities = np.array(df['city'])
list_of_countries = np.array(df['country'])

city = input('Enter your city')
word = spell.correction(city)
word = word.capitalize() # capitalize the first alphabet

if word==city:
    print("Correct city entered")
else:
    if word in list_of_cities or word in list_of_countries:
        print("May be you mean",word)
    else:
        print("You entered the wrong city")
