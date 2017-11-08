# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-08 00:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171017_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 21, 39, 26, 867444)),
        ),
        migrations.AlterField(
            model_name='follow',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 21, 39, 26, 867444)),
        ),
        migrations.AlterField(
            model_name='game',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 21, 39, 26, 867444)),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 21, 39, 26, 867444)),
        ),
    ]
