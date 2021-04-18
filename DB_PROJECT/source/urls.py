from django.contrib import admin
from django.urls import path, include
from . import views
from .views import my_course
  
app_name = 'uploader'
  
urlpatterns = [
    