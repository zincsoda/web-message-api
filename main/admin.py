from django.contrib import admin
from main.models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'created_at','message', 'users_name')
admin.site.register(Message, MessageAdmin)
