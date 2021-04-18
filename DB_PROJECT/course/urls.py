from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('mycourse/',views.mycourse),
    path('source/<str:id>',views.course_source, name='course_source'),
    path('add_course/',views.add_course),
    path('course_deteils/<str:id>',views.course_deteils, name = 'course_deteils'),
    path('course_modify/<str:id>',views.course_modify, name = 'course_modify'),
    path('quit_course/<str:id>',views.quit_course, name = 'quit_course'),
]