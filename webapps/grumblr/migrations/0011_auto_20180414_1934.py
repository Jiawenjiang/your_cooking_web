# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-14 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0010_profile_voting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_changed',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]