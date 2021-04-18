from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('course_id','name','course_teachers')
    actions_on_top=True
    search_fields=['name']
