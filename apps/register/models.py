from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.db import models

from django.db.models import CASCADE

from products.models import Products

from star_ratings.models import Rating


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES,null=True)

    user_name = models.CharField(max_length=100)
def Average(lst):
    return sum(lst) / len(lst)
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=CASCADE)

    author = models.ForeignKey(Products, on_delete=CASCADE, null=True)
    # isSeller = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # prfoielpic = models.ImageField(blank=False,
    #                                null=True,
    #                                upload_to='profile/' +first_name+user.username)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user.username

    def setSeller(self):
        self.user.isSeller=True



