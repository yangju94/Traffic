# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-06 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrash', '0026_vehicledata_death_sen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='ROUTE',
            field=models.CharField(choices=[('9', '\u672a\u77e5'), ('1', '\u56fd\u9053'), ('2', '\u7701\u9053'), ('3', '\u53bf\u9053'), ('4', '\u4e61\u6751\u9053\u8def'), ('5', '\u9ad8\u901f\u516c\u8def'), ('6', '\u57ce\u5e02\u9053\u8def-\u4e3b\u5e72\u9053'), ('7', '\u57ce\u5e02\u9053\u8def-\u5176\u4ed6'), ('8', '\u5176\u4ed6')], default='\u672a\u77e5', help_text='\u9053\u8def\u6807\u5fd7', max_length=10),
        ),
    ]