# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-20 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0005_auto_20171019_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='last_changed',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='last_changed',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
