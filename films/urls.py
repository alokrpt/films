# films/urls.py
from django.urls import path
from . import views
from django.contrib import admin


app_name = 'films'
urlpatterns = [
    path('', views.main, name='main'),
    path('user_info/', views.user_info, name='user_info'),
    path('user_form/', views.user_form, name= 'user_form'),
    path('<int:id>/details', views.details, name='details'),
    
]