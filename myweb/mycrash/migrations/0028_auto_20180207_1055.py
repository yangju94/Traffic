# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-07 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrash', '0027_auto_20180206_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='VEDIO',
            field=models.CharField(choices=[('0', '\u65e0\u89c6\u9891'), ('1', '\u56fa\u5b9a\u5f0f\u76d1\u63a7\u5f55\u50cf'), ('2', '\u884c\u8f66\u8bb0\u5f55\u4eea'), ('3', '\u56fa\u5b9a\u5f0f\u4e0e\u884c\u8f66\u8bb0\u5f55\u4eea\u5747\u6709'), ('4', '3\u79cd\u89c6\u9891\u53ca\u4ee5\u4e0a'), ('8', '\u5176\u4ed6\u89c6\u9891\u8bb0\u5f55\u8bbe\u5907'), ('9', '\u672a\u77e5')], default='0', help_text='\u8bb0\u5f55\u6b64\u6848\u4ef6\u6216\u4e0e\u6b64\u6848\u4ef6\u76f8\u5173\u7684\u89c6\u9891', max_length=15),
        ),
    ]
