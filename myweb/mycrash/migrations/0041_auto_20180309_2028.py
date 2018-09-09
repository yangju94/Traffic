# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-09 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mycrash', '0040_auto_20180308_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='persondata',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vehicledata',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='persondata',
            name='EJECTION',
            field=models.CharField(choices=[('0', '\u672a\u5f39\u51fa'), ('1', '\u90e8\u5206\u5f39\u51fa'), ('2', '\u5b8c\u5168\u5f39\u51fa'), ('3', '\u5f39\u51fa-\u7a0b\u5ea6\u672a\u77e5'), ('8', '\u4e0d\u9002\u7528'), ('9', '\u672a\u77e5')], default=8, help_text='\u8be5\u4eba\u5458\u4ece\u8f66\u5185\u5f39\u51fa\u72b6\u51b5\uff08\u4ec5\u9650\u6c7d\u8f66\uff09', max_length=10),
        ),
    ]