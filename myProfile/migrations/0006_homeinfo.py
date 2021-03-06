# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-18 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import myProfile.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myProfile', '0005_aboutinfo_aboutuptoinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50)),
                ('subheader', models.CharField(max_length=200)),
                ('cv', models.FileField(upload_to='cv/', validators=[myProfile.validators.validate_file_extension])),
            ],
        ),
    ]
