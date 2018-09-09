# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-19 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrash', '0006_auto_20180119_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='url',
        ),
        migrations.AddField(
            model_name='photo',
            name='DAY',
            field=models.PositiveIntegerField(default=1, help_text='\u53f7\u6570'),
        ),
        migrations.AddField(
            model_name='photo',
            name='MONTH',
            field=models.PositiveIntegerField(default=1, help_text='\u6708\u4efd'),
        ),
        migrations.AddField(
            model_name='photo',
            name='URL',
            field=models.URLField(default='', help_text='\u73b0\u573a\u7167\u7247\u94fe\u63a5\u5730\u5740'),
        ),
        migrations.AddField(
            model_name='photo',
            name='YEAR',
            field=models.PositiveIntegerField(default=2018, help_text='\u5e74\u4efd'),
        ),
    ]