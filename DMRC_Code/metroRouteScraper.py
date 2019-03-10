import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def getStation(i):
    try:
        s = route[i].contents[0].contents[0]
        return s
    except:
        return ""

# url = "https://delhimetrorail.info/peera-garhi-delhi-metro-station-to-dwarka-mor-delhi-metro-station?live=true"
#URL Formation
flag = 1
while flag == 1:
    try:
        a = "https://delhimetrorail.info/"
        fromS = input("Enter Start Station : ")
        fromStation = fromS.lower().replace(" ","-")
        toS = input("Enter Destination Station : ")
        toStation = toS.lower().replace(" ","-")
        b = "-delhi-metro-station"

        url = a + fromStation + b + "-to-" + toStation + b + "?live=true"
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        route = soup.find("div",{"id":"divCanvas"})
        route = route.findAll("div")
        flag = 0
    except:
        print("Enter valid Station names or check your internet connection")
        flag = 1


i = 1
prev = "1"
s = getStation(i)
while s.lower() != toS.lower():
    if s != "":
        if prev == s:
            print()
            print("Change Station Here")
            print("")
        print(s,end = " -> ")
        prev = s
    i += 1
    s = getStation(i)
print(s)

