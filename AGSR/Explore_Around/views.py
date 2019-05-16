# filename: first_site/votings/views.py

from django.shortcuts import render
from django.http import HttpResponse

from bs4 import BeautifulSoup
import requests

def home(request):
	return render(request, 'Explore_Around/Home.html')
def placeinfo(request):
	url = 'https://www.britannica.com/place/delhi'
	res = requests.get(url)
	soup = BeautifulSoup(res.text,'lxml')
	info = soup.find('section',{'id':'ref1'})
	para = info.find_all('p')
	info = ""
	for i in para:
		info = info + i.text
	inf = info		# Knowing which decides 
	s = {'info':inf}
	return render(request, 'Explore_Around/PlaceInfo.html',s)

	
def distance(request):
	return render(request, 'Explore_Around/Distance.html')
def metro(request):
	return render(request, 'Explore_Around/Metro.html')
def hotel(request):
	return render(request, 'Explore_Around/Hotel.html')
def weather(request):
	return render(request, 'Explore_Around/Weather.html')
def login(request):
	return render(request, 'Explore_Around/Login.html')
def mailus(request):
	return render(request, 'Explore_Around/MailUs.html')
def aboutus(request):
	return render(request, 'Explore_Around/AboutUs.html')
