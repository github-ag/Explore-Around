from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def getDriver():
    GOOGLE_CHROME_BIN = os.getenv('GOOGLE_CHROME_BIN')
    CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = GOOGLE_CHROME_BIN

    driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=chrome_options)
    return driver

def getDriverTest():
    options = Options()
    options.headless = True

    driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe', chrome_options=options)
    return driver
