# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 13:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0003_post_authors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creation_date',
            new_name='date_creation',
        ),
    ]
