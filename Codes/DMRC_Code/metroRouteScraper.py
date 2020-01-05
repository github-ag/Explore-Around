import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def getStation(i,route):
    try:
        s = route[i].contents[0].contents[0]
        return s
    except:
        return ""

# url = "https://delhimetrorail.info/peera-garhi-delhi-metro-station-to-dwarka-mor-delhi-metro-station?live=true"
#URL Formation
def metroRoute(fromS,toS):
    route = ""
    try:
        a = "https://delhimetrorail.info/"
        fromStation = fromS.lower().replace(" ","-")
        toStation = toS.lower().replace(" ","-")
        b = "-delhi-metro-station"

        url = a + fromStation + b + "-to-" + toStation + b + "?live=true"
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        route = soup.find("div",{"id":"divCanvas"})
        route = route.findAll("div")
    except:
        return "Enter valid Station names or check your internet connection"


    i = 1
    prev = "1"
    s = getStation(i,route)
    finalRoute = ""
    while s.lower() != toS.lower():
        if s != "":
            if prev == s:
                finalRoute += "\nChange Station Here\n" + s + " -> "
            else:
                finalRoute += s + " -> "
            prev = s
        i += 1
        s = getStation(i,route)
    finalRoute += s
    return finalRoute
