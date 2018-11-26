from __future__ import unicode_literals
from datetime import datetime

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import CASCADE
from django.db.models.signals import pre_save, post_save

from django.contrib.auth.models import User
from django.db import models




def download_media_location(instance, filename):
    return "%s/%s" %(instance.slug, filename)


class Products(models.Model):

    user=models.ForeignKey(User,on_delete=models.PROTECT)
    title=models.CharField(blank=False,default='.',max_length=50)
    choices=(
    ('Electronics', 'Electronics'),
    ('Books', 'Books'),
    ('Services', 'Services'),
    ('Others','Others')
)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    tag=models.CharField(choices=choices, max_length=20, blank=False, default='Others')

    media = models.ImageField(blank=False,
                              null=True,
                              upload_to='articles_pictures/%Y/%m/%d/')
    description=models.TextField(blank=False,default='no descripiton')
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)



    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        return self.slug

    def get_price(self):
        return self.price




from .utils import unique_slug_generator

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = create_slug(instance)
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_post_receiver, sender=Products)




