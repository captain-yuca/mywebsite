# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-17 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProfile', '0003_auto_20171118_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='projects/empty_project.jpg', upload_to='projects/'),
        ),
    ]