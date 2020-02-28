# filename: first_site/votings/views.py
from main.forms import *
from django.shortcuts import render
from django.http import HttpResponse
from Codes import SendPersonalizedMail, DMRC_Code, CalculateDistance, place_info, WeatherDetails
from Codes.DMRC_Code import metroFareCSV, metroRouteScraper
import os

# import redis
# from rq import Worker, Queue, Connection
# from rq.job import Job
# 
# listen = ['high', 'default', 'low']
# 
# redis_url = os.getenv('REDIS_URL')
# 
# conn = redis.from_url(redis_url)
# with Connection(conn):
#     worker = Worker(map(Queue, listen))
#     worker.work()
# 
# q = Queue(connection = conn)

def home(request):
    return render(request, 'main/Home.html')

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
            context = {
                'info': place_info.getPlaceInfo(str(form.cleaned_data['placeName']))
            }
            return render(request, 'main/PlaceInfo.html', context)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = {
            'form': NameForm()
        }
    
    return render(request, 'main/PlaceInfo.html', form)


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
            context = {
                'info':inf
            }
            return render(request, 'main/Distance.html', context)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = {
            'form': TwoForm()
        }
    
    return render(request, 'main/Distance.html', form)

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
            
            # price = metroFareCSV.metroFare(fromNameCurr,toNameCurr)
            context = {
                'route': metroRouteScraper.metroRoute(fromNameCurr, toNameCurr)
            }
            return render(request, 'main/Metro.html', context)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = {
            'form': TwoForm()
        }
    
    return render(request, 'main/Metro.html', form)

def hotel(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # info = WeatherDetails.weather(str(form.cleaned_data['placeName']))
            info = "Hello User, Welcome to hotel page"
            context = {
                'info':info
            }
            return render(request, 'main/Hotel.html', context)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = {
            'form': NameForm()
        }
    
    return render(request, 'main/Hotel.html', form)

def weather(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            context = {
                'info': WeatherDetails.weather(str(form.cleaned_data['placeName']))
            }
            return render(request, 'main/Weather.html', context)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = {
            'form': NameForm()
        }
    
    return render(request, 'main/Weather.html', form)

def login(request):
    return render(request, 'main/Login.html')

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
            name = str(form.cleaned_data['name'])
            mail_id = str(form.cleaned_data['mail'])
            subject = str(form.cleaned_data['subject'])
            query = str(form.cleaned_data['query'])
            # q.enqueue_call(
            #     func = SendPersonalizedMail.sendMailFunction, args = (name, mail_id, subject, query), result_ttl = 600, timeout = '10m'
            # )

            # context = {
            #     'info': 'Our team will contact you soon'
            # }
            # # ===================================
            mail_result = SendPersonalizedMail.sendMailFunction(name, mail_id, subject, query)
            context = {
                'info': mail_result
            }
            return render(request, 'main/MailUs.html', context)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = {
            'form': MailForm()
        }
    
    return render(request, 'main/MailUs.html', form)

def aboutus(request):
    return render(request, 'main/AboutUs.html')
