# Generated by Django 2.1.2 on 2018-11-20 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='media',
            field=models.ImageField(blank=True, null=True, upload_to='articles_pictures/%Y/%m/%d/'),
        ),
    ]