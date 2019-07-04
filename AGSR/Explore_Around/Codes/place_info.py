from bs4 import BeautifulSoup
import requests

def getPlaceInfo(city):
	try:
		url = 'https://www.britannica.com/place/{}'.format(city)
		res = requests.get(url)
		soup = BeautifulSoup(res.text,'lxml')
		info = soup.find('section',{'id':'ref1'})
		para = info.find_all('p')
		curr = ""
		for i in para:
			curr = curr + i.text + '\n'
		return curr
	except:
		return "Please check your internet connection"
