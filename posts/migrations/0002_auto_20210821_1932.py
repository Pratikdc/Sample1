# Generated by Django 3.1 on 2021-08-21 14:02

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='like_count'),
        ),
    ]
