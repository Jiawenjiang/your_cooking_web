# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 23:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0003_remove_post_can_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='content',
        ),
    ]
