# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-05 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrash', '0025_auto_20180205_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicledata',
            name='DEATH_SEN',
            field=models.PositiveIntegerField(default=99, help_text='\u8be5\u8f66\u8f86\u5185\u5f53\u573a\u6b7b\u4ea1\u4eba\u6570\uff08\u4e0d\u542b\u6551\u62a4\u9014\u4e2d\u6b7b\u4ea1\u7684\u4eba\u6570\uff09\uff0c99\u672a\u77e5'),
        ),
    ]
