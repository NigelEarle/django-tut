# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-16 21:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 6, 16, 21, 1, 39, 602622, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
