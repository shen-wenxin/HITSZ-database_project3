from django.contrib import admin
from django.urls import path, include
from . import views
from .views import upload
  
app_name = 'uploader'
  
urlpatterns = [
    path('upload/',views.upload),
    path('list/',views.sourcelist),
    path('mysource_list/',views.mysource_list),
    
]
    