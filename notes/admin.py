from django.contrib import admin

# Register your models here.
from .models import Notes


class PostModelAdmin(admin.ModelAdmin):


    class Meta:
        model = Notes


admin.site.register(Notes, PostModelAdmin)
