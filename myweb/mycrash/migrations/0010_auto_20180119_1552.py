# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-19 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrash', '0009_auto_20180119_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident',
            name='NUM',
            field=models.CharField(default='001', help_text='\u5730\u533a\u6848\u4ef6\u7f16\u53f7', max_length=5),
        ),
        migrations.AlterField(
            model_name='accident',
            name='NAME',
            field=models.CharField(default='\u70b9\u51fb\u4fdd\u5b58\u4f1a\u81ea\u52a8\u7f16\u7801', help_text='\u6848\u4ef6\u7f16\u7801', max_length=30),
        ),
    ]
