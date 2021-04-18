from django.contrib import admin
from .models import FileInfo


@admin.register(FileInfo)
class FileInfoAdmin(admin.ModelAdmin):
    list_display=('file_name','remarks','upload_time',
                    'uploader_id','download_times','file_info','course')
    actions_on_top=True
    search_fields=['file_name']



