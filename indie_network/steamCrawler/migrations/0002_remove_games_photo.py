# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-05 15:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steamCrawler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='photo',
        ),
    ]
