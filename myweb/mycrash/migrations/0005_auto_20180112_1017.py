# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-12 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrash', '0004_auto_20180112_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='NAME',
            field=models.CharField(default='xxxxxx xxxx', help_text='\u6848\u4ef6\u7f16\u7801', max_length=30),
        ),
        migrations.AlterField(
            model_name='persondata',
            name='description',
            field=models.CharField(default='xxxxxx xxxx Vxx Oxx', help_text='\u4eba\u5458\u7f16\u7801', max_length=30),
        ),
        migrations.AlterField(
            model_name='vehicledata',
            name='decription',
            field=models.CharField(default='xxxxxx xxxx Vxx', help_text='\u8f66\u8f86\u7f16\u7801', max_length=30),
        ),
    ]