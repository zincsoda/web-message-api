from rest_framework import serializers
from main.models import *


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('uuid', 'created_at', 'message','users_name', 'users_email', 'users_avatar_url')
        read_only_fields = ('uuid', 'created_at')
