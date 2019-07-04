# filename: first_site/votings/urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.home, name='home'),
	path('placeinfo/', views.placeinfo, name='placeinfo'),
	path('distance/', views.distance, name='distance'),
	path('metro/', views.metro, name='metro'),
	path('hotel/', views.hotel, name='hotel'),
	path('weather/', views.weather, name='weather'),
	path('login/', views.login, name='login'),
	path('mailus/', views.mailus, name='mailus'),
	path('aboutus/', views.aboutus, name='aboutus'),

	# path('', views.detail, name='detail'),
	# path('<int:question_id>/results/', views.results, name='results'),
	# path('<int:question_id>/vote/', views.vote, name='vote'),
]