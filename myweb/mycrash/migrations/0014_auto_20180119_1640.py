# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-19 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrash', '0013_auto_20180119_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondata',
            name='PER_NO',
            field=models.CharField(default='01', help_text='\u8be5\u4eba\u5458\u7f16\u53f7\uff0c\u884c\u4eba\u4e0e\u4e58\u5458\uff08\u542b\u9a7e\u9a76\u5458\uff09\u5206\u5f00\u7f16\u7801', max_length=10),
        ),
        migrations.AlterField(
            model_name='vehicledata',
            name='VEH_NO',
            field=models.CharField(default='00', help_text='\u4e8b\u6545\u8f66\u8f86\u7f16\u53f7\uff0c\u884c\u4eba\u4e3a00,2\u4f4d\u6570', max_length=5),
        ),
    ]
