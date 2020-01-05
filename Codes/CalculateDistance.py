from bs4 import BeautifulSoup
import requests, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def calDistance(starting, destination):
    url = 'https://distancecalculator.globefeed.com/India_Distance_Result.asp?vr=apes&fromplace={},India&toplace={},India'.format(starting,destination)

    GOOGLE_CHROME_BIN = os.getenv('GOOGLE_CHROME_BIN')
    CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = GOOGLE_CHROME_BIN

    curr = ""
    try:
        driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=chrome_options)
        driver.get(url)

        res = driver.execute_script("return document.documentElement.outerHTML")

        # res = requests.get(url)
        soup = BeautifulSoup(res,'lxml')
        dist = soup.find('div',{'class':'panel panel-primary'})

        driving_distance = dist.find('span',{'id':'drvDistance'})
        duration = dist.find('span',{'id':'drvDuration'})
        route = dist.find('span',{'id':'drvRoute'})
        straight = dist.find('span',{'id':'straightDist'})

        curr = '\ndriving distance :' + driving_distance.text + '\nduration :' + duration.text
        curr = curr + '\nroute :'+route.text + '\nstraight line distance or air distance :' + straight.text
    except:
        curr = "Error getting distance \n Please Check your internet connection"
    return curr
