from django.db import models
import uuid
from main.utils import get_gravatar_url

class Message(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200, blank=True, null=True)
    users_name = models.CharField(max_length=200, blank=True, null=True)
    users_email = models.CharField(max_length=200, blank=True, null=True)
    users_avatar_url = models.CharField(max_length=400, blank=True, null=True)

    def __unicode__(self):
        return self.message

    # def save(self, *args, **kwargs):
    #     if not self.users_avatar_url:
    #         gravatar_url = "https://www.wiredwizards.org/wp-content/uploads/2016/03/generic_avatar.jpg" #get_gravatar_url(self.users_email)
    #         self.users_avatar_url = gravatar_url
    #         super(Message, self).save(*args, **kwargs)