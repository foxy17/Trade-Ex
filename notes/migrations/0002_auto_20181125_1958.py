# Generated by Django 2.1.2 on 2018-11-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noteimages',
            name='image',
            field=models.ImageField(null=True, upload_to='Notes/'),
        ),
    ]