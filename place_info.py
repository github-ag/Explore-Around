from bs4 import BeautifulSoup
import requests
city = input('Enter your city : ')
url = 'https://www.britannica.com/place/{}'.format(city)
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
info = soup.find('section',{'id':'ref1'})
para = info.find_all('p')

for i in para:
    print(i.text)
    print('\n')
