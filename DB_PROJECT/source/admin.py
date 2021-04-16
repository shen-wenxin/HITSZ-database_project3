from django.contrib import admin
from .models import FileInfo,CourseInfo


@admin.register(FileInfo)
class FileInfoAdmin(admin.ModelAdmin):
    list_display=('file_name','remarks','upload_time',
                    'uploader_id','download_times','file_info')
    actions_on_top=True
    search_fields=['file_name']


@admin.register(CourseInfo)
class CourseInfoAdmin(admin.ModelAdmin):
    list_display=('course_id','name','course_teachers')
    actions_on_top=True
    search_fields=['name']
