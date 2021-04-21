from django.contrib import admin
from django.urls import path, include
from . import views
  
  
urlpatterns = [
    path('send_message/',views.send_message, name='send_message'),
    path('recieve_message/',views.recieve_message, name='recieve_message'),
    path('sended_message/',views.sended_message,name='delete_message'),
    path('message_info/<int:id>',views.message_info, name='message_info'),
    path('delete_message/<int:id>',views.delete_message,name='delete_message'),
    path('delete_message_send/<int:id>',views.delete_message_send,name='delete_message_send'),
]