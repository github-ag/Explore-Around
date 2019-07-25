# filename: first_site/votings/views.py
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse
from .Codes import SendPersonalizedMail, DMRC_Code, CalculateDistance, place_info, WeatherDetails
from .Codes.DMRC_Code import metroFareCSV, metroRouteScraper


def home(request):
    return render(request, 'Explore_Around/Home.html')

def placeinfo(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            info = place_info.getPlaceInfo(str(form.cleaned_data['placeName']))
            inf = info		# Knowing which decides 
            s = {'info':inf}
            return render(request, 'Explore_Around/PlaceInfo.html',s)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    
    return render(request, 'Explore_Around/PlaceInfo.html', {'form': form})


def distance(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TwoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            fromNameCurr = str(form.cleaned_data['fromName'])
            toNameCurr = str(form.cleaned_data['toName'])
            
            info = CalculateDistance.calDistance(fromNameCurr, toNameCurr)
            info = info.split('\n')
            inf = ""
            for i in info:
                inf += i + "\n"		# \n not working
            s = {'info':inf}
            return render(request, 'Explore_Around/Distance.html',s)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TwoForm()
    
    return render(request, 'Explore_Around/Distance.html', {'form': form})

def metro(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TwoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            fromNameCurr = str(form.cleaned_data['fromName'])
            toNameCurr = str(form.cleaned_data['toName'])
            
            #price = metroFareCSV.metroFare(fromNameCurr,toNameCurr)
            route = metroRouteScraper.metroRoute(fromNameCurr,toNameCurr)
            
            s = {'route':route}
            return render(request, 'Explore_Around/Metro.html',s)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TwoForm()
    
    return render(request, 'Explore_Around/Metro.html', {'form': form})

def hotel(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # info = WeatherDetails.weather(str(form.cleaned_data['placeName']))
            info = "Hello User, Welcome to hotel page"
            s = {'info':info}
            return render(request, 'Explore_Around/Hotel.html',s)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    
    return render(request, 'Explore_Around/Hotel.html', {'form': form})

def weather(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            info = WeatherDetails.weather(str(form.cleaned_data['placeName']))
            s = {'info':info}
            return render(request, 'Explore_Around/Weather.html',s)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    
    return render(request, 'Explore_Around/Weather.html', {'form': form})

def login(request):
    return render(request, 'Explore_Around/Login.html')

def mailus(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            nameCurr = str(form.cleaned_data['name'])
            mailCurr = str(form.cleaned_data['mail'])
            subjectCurr = str(form.cleaned_data['subject'])
            queryCurr = str(form.cleaned_data['query'])
            
            inf = SendPersonalizedMail.sendMailFunction(nameCurr,mailCurr,subjectCurr,queryCurr)
            
            s = {'info':inf}
            return render(request, 'Explore_Around/MailUs.html',s)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MailForm()
    
    return render(request, 'Explore_Around/MailUs.html', {'form': form})

def aboutus(request):
    return render(request, 'Explore_Around/AboutUs.html')
