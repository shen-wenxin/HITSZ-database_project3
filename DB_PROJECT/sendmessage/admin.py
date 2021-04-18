from django.contrib import admin
from .models import MessageInfo

@admin.register(MessageInfo)
class MessageInfoAdmin(admin.ModelAdmin):
    list_display=('send_time',
                  'sender_id',
                  'reciever_id',
                  'theme',
                  'text',
                  'read_flag',
                  'sender_delete',
                  'reciever_delete')
    actions_on_top=True
    search_fields=['theme']


