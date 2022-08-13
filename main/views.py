from django.http import HttpResponse
from django.shortcuts import render
from main.models import Message
from main.serializers import MessageSerializer
from rest_framework import viewsets
from django.template import loader
from main.consumers import PracticeConsumer
from asgiref.sync import async_to_sync
import subprocess
from channels.layers import get_channel_layer


def test(request):
    print("testing ...")
    return HttpResponse("Hello")

def power_on(request):
    subprocess.call('ls')
    # subprocess.call('vcgencmd display_power 1')
    return HttpResponse("Power on")

def power_off(request):
    # subprocess.call('vcgencmd display_power 0')    
    return HttpResponse("Power off")

def message(request, message_string):
    
    channel_layer = get_channel_layer()
    channel_group_name = "channel_group_name"
    async_to_sync(channel_layer.group_send)(channel_group_name, {'type': 'notify', 'content':message_string})

    return HttpResponse("Message sent")

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    print(serializer_class)