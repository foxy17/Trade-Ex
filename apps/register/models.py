from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from django.db.models import CASCADE


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user.username

