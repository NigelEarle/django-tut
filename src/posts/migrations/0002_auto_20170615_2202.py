# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-15 22:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='content',
        ),
    ]
