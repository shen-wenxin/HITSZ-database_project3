"""DB_PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user.views import register,login,index,logout
from source.views import upload,sourcelist,download
from sendmessage.views import send_message,recieve_message,message_info,delete_message,sended_message,delete_message_send
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register),
    path('login/',login),
    path('logout/',logout),
    path('index/',index),
    path('upload/',upload),
    path('list/',sourcelist),
    path('download/<int:id>',download, name='download'),
    path('send_message/',send_message, name='send_message'),
    path('recieve_message/',recieve_message, name='recieve_message'),
    path('message_info/<int:id>',message_info, name='message_info'),
    path('delete_message/<int:id>',delete_message,name='delete_message'),
    path('delete_message_send/<int:id>',delete_message_send,name='delete_message_send'),
    path('sended_message/',sended_message,name='delete_message'),
    path('course/',include('course.urls'))

    
]
