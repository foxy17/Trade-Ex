from __future__ import unicode_literals

from django.db.models.signals import pre_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from slugify import slugify


def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)


class PostQuerySet(models.query.QuerySet):


    def published(self):
        return self.filter(publish__lte=timezone.now())


class PostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return PostQuerySet(self.model, using=self._db)

    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return self.get_queryset().published()


class Post (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(blank=False,default='.',max_length=50)
    choices=(
    ('Electronics', 'Electronics'),
    ('Books', 'Books'),
    ('Services', 'Services'),
    ('Others','Others')
)
    price=models.IntegerField(blank=False,default=0)
    tag=models.CharField(choices=choices, max_length=20, blank=False, default='Others')

    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,

                             )
    description=models.TextField(blank=False,default='no descripiton')
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    content = models.TextField()


    objects=PostManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


from .utils import unique_slug_generator

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = create_slug(instance)
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)