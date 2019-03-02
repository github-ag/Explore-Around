from bs4 import BeautifulSoup
import requests
from selenium import webdriver
starting = input('Enter starting location')
destination = input('enter the destination')
url = 'https://distancecalculator.globefeed.com/India_Distance_Result.asp?vr=apes&fromplace={},India&toplace={},India'.format(starting,destination)

driver = webdriver.Chrome('C:/Users/Abhishek Garg/Downloads/chromedriver_win32/chromedriver.exe')
driver.get(url)

res = driver.execute_script("return document.documentElement.outerHTML")

#res = requests.get(url)
soup = BeautifulSoup(res,'lxml')
dist = soup.find('div',{'class':'panel panel-primary'})

driving_distance = dist.find('span',{'id':'drvDistance'})
duration = dist.find('span',{'id':'drvDuration'})
route = dist.find('span',{'id':'drvRoute'})
straight = dist.find('span',{'id':'straightDist'})


print('driving distance :',driving_distance.text)
print('duration :',duration.text)
print('route :',route.text)
print('straight line distance or air distance :',straight.text)
#print(dist.text)
