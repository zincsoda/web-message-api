from django.urls import re_path

from main import consumers

websocket_urlpatterns = [
    re_path(r'ws/test/$', consumers.PracticeConsumer.as_asgi()),
]