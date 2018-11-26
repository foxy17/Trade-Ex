from __future__ import unicode_literals
from datetime import datetime

from django.utils.functional import cached_property
from django.utils.translation import ugettext as _
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import CASCADE
from django.db.models.signals import pre_save, post_save
from django.utils.six import python_2_unicode_compatible
from slugify import slugify
from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField


def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset()
@python_2_unicode_compatible
class Notes(models.Model):

    user=models.ForeignKey(User,on_delete=models.PROTECT)
    topic=models.CharField( max_length=30, blank=False, default='Not Selected')
    choices=(
    ('Subject1', 'Subject1'),
    ('Subject2', 'Subject2'),
    ('Subject3', 'Subject3'),
    ('Subject4','Subject4')
)
    image = models.ImageField(_('image'),
                              upload_to='Notes/',null=True
                              )
    image1 = models.ImageField(_('image1'),
                              upload_to='Notes/',null=True
                              )
    image2 = models.ImageField(_('image2'),
                              upload_to='Notes/',null=True
                              )
    image3 = models.ImageField(_('image3'),
                              upload_to='Notes/',null=True
                              )

    subject=models.CharField(choices=choices, max_length=20, blank=False, default='Others')
    notes=models.TextField(blank=False,default='no descripiton')
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    objects = models.Manager()
    active = ActiveManager()
    @cached_property
    def image_count(self):
        return self.image_set.count()
    @cached_property
    def featured_image(self):
        return self.image_set.all().first()
    def __unicode__(self):
        return self.topic


    def get_absolute_url(self):
        return self.slug

    def first_image(self):
        # code to determine which image to show. The First in this case.
        return self.images.first()
    def all_images(self):
        return self.images.all()



from .utils import unique_slug_generator

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = create_slug(instance)
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_post_receiver, sender=Notes)




