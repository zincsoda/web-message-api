from django.http import HttpResponse
from django.shortcuts import render
from main.models import Message
from main.serializers import MessageSerializer
from rest_framework import viewsets
from django.template import loader
from main.consumers import PracticeConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import subprocess

# from rest_framework import permissions

def test(request):
    print("testing ...")
    return HttpResponse("Hello")

def power_on(request):
    subprocess.call('ls')
    # subprocess.call('vcgencmd display_power 1')
    return HttpResponse("Power on")

def power_off(request):
    subprocess.call('ls')
    # subprocess.call('vcgencmd display_power 0')
    return HttpResponse("Power off")


# async def index(request):
#     print("debug 2")
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#             f"{request.user.id}-message", {"type": "send_message",
#                                            "text": "socket_message"}
#         )

#     return render(request, 'main/index.html')

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = [permissions.IsAuthenticated]

# def render_message(request, uuid):
#     message = Message.objects.get(uuid=uuid)
#     import random
#     r = lambda: random.randint(0,255)
#     background_rgb = '#%02X%02X%02X' % (r(),r(),r())
#     template_dict = {
#         "message": message.message,
#         "created_at": message.created_at,
#         "users_name": message.users_name,
#         "users_avatar_url": message.users_avatar_url,
#         "background_rgb": background_rgb
#     }
#     return render('index.html', template_dict)

