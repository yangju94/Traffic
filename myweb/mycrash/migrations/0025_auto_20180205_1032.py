# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-05 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrash', '0024_auto_20180205_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicledata',
            name='DEATH',
            field=models.PositiveIntegerField(default=99, help_text='\u8be5\u8f66\u8f86\u4e2d\u7684\u603b\u6b7b\u4ea1\u4eba\u6570\uff08\u4e0e\u6b64\u6b21\u4e8b\u6545\u76f8\u5173\u7684\u6b7b\u4ea1\u4eba\u6570\u90fd\u7edf\u8ba1\u5728\u5185\uff09,99\u4e0d\u9002\u7528'),
        ),
    ]
