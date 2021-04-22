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
from user.views import register,login,index,logout,user_info_teacher,user_info_student
from source.views import upload,sourcelist,download,deletesource
from sendmessage.views import send_message,recieve_message,message_info,delete_message,sended_message,delete_message_send
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register),
    path('login/',login),
    path('logout/',logout),
    path('index/',index),
    path('user_info_teacher/',user_info_teacher),
    path('user_info_student/',user_info_student),
    path('source/',include('source.urls')),
    path('source/deletesource/<int:id>',deletesource, name='deletesource'),
    path('source/download/<int:id>',download, name='download'),
    path('message/',include('sendmessage.urls')),
    path('course/',include('course.urls'))

    
]
