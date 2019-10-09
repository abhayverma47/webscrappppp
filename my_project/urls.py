from django.urls import path
from . import views


# what this says is if we visit home page like www.abhayverma.com them take us to views of home

urlpatterns = [
    path('', views.home, name='home'),
    path('new_search', views.new_search, name='new_search'),
    path('about', views.about, name='about'),
]