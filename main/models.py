from django.db import models
import uuid
from main.utils import get_gravatar_url
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
class Message(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200, blank=True, null=True)
    users_name = models.CharField(max_length=200, blank=True, null=True)
    users_email = models.CharField(max_length=200, blank=True, null=True)
    users_avatar_url = models.CharField(max_length=400, blank=True, null=True)

    def __unicode__(self):
        return self.message

    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        channel_group_name = "channel_group_name"
        async_to_sync(channel_layer.group_send)(channel_group_name, {'type': 'notify', 'content':self.message})

        super(Message, self).save(*args, **kwargs)