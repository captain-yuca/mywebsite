# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-18 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProfile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image_url',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='static/images/profile.jpg', upload_to='static/images/projects'),
        ),
    ]
