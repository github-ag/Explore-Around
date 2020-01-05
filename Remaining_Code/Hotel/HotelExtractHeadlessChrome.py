from selenium import webdriver
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests

# For headless chrome
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True

one = "https://www.hotelplanner.com/Hotels-Near-Me#search/"
nameToBeSearched = ""
two = "/none/none/"
checkInDate = ""
three = "/"
checkOutDate = ""
four = "/default/ASC/ASC/ASC/0/none/none/none/0/0/0/0/0/0/0/0/0/0/0/0/0/none/none/NaN/5/none/none/none/"
noOfRooms = ""
five = "/1/1/0/1/1/results/0/"
url = one + nameToBeSearched + two + checkInDate + three + checkOutDate + four + noOfRooms + five

url = "https://www.hotelplanner.com/Hotels-Near-Me#search/Bihar%20-%20India/none/none/03-02-2019/03-03-2019/default/ASC/ASC/ASC/0/none/none/none/0/0/0/0/0/0/0/0/0/0/0/0/0/none/none/NaN/5/none/none/none/4/1/1/0/1/1/results/0/"


driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe', chrome_options=options)
# "chrome_options" parameter added for headless chrome
driver.get(url)
res = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(res, "lxml")


Ad = soup.find("div",{'id':'MainTable'})
Ad = Ad.find("div",{'id':'ContentTable'})
Ad = Ad.find("form",{'id':'frmGroup'})
Ad = Ad.find("div",{'id':'Content'})
Ad = Ad.find("div",{'id':'Rates-Column'})
Ad = Ad.find("div",{'class':'container_hp'})
Ad = Ad.find("div",{'id':'Rates'})
Ad = Ad.find("div",{'id':'hotelHOTEL249851823001194'})
# Ad comes to be None if webdriver not used

Ad = Ad.find("div",{'class':'hotel-rates'})
Ad = Ad.find("div",{'class':'description-column'})
Ad = Ad.find("span",{'class':'address'})

print(Ad.contents[0])

print("LOL")

input()
