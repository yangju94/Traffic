# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-06 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrash', '0037_auto_20180306_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondata',
            name='DREASON',
            field=models.CharField(choices=[('1', '\u5934\u90e8'), ('2', '\u80f8\u90e8'), ('3', '\u8179\u90e8'), ('4', '\u80f8\u90e8\u53ca\u8179\u90e8'), ('8', '\u7efc\u5408'), ('9', '\u672a\u77e5/\u4e0d\u9002\u7528')], default='9', help_text='\u8eab\u4f53\u54ea\u4e2a\u90e8\u4f4d\u521b\u4f24\u5bfc\u81f4\u6b7b\u4ea1', max_length=10),
        ),
    ]
