# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-14 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0009_auto_20180414_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='voting',
            field=models.ManyToManyField(related_name='_profile_voting_+', to='grumblr.Post'),
        ),
    ]
