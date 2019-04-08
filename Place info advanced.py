import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
class node:
    def __init__(self):
        self.nodes = dict()
        self.is_leaf = False

    def insert_many(self,str):
        for word in str.split(" "):
            for w in re.split('\.|, ',word):
                self.insert(w)

    def insert(self,word):
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = node()
            curr = curr.nodes[char]
        curr.is_leaf=True

    def find(self,word):
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf


city = input('Enter your city : ')
url = 'https://www.britannica.com/place/{}'.format(city)
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
info = soup.find('section',{'id':'ref1'})
para = info.find_all('p')

for i in para:
    print(i.text)
    print('\n')

messages=[]
for i in para:
    for line in i.text.split('.'):
        messages.append(line)

df = pd.DataFrame()
df['messages'] = messages
df['length'] = df['messages'].apply(len)


i=0
for mess in df['messages']:
    list = mess.split(' ')
    if (len(list)>1 and list[1] =='Area') or len(mess)<df['length'].mean():
        df=df.drop([i])
    i=i+1;

root = node()
for mess in df['messages']:
    root.insert_many(mess)
    print(mess,'.')
    print('\n')

word = input("Enter word you want to search-> ")
if(root.find(word)):
    print(word,' is present in the information')
else:
    print('Sorry! this word is not present in the information')
