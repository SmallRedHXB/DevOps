# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 07:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0005_history_hosts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='hosts',
        ),
    ]
