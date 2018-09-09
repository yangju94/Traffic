# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-12 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrash', '0041_auto_20180309_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident',
            name='ARR_MIN',
            field=models.CharField(default=99, help_text='\u533b\u7597\u670d\u52a1\u5230\u8fbe\u5206\u949f\u6570\uff0c99\u4e3a\u672a\u77e5', max_length=5),
        ),
        migrations.AlterField(
            model_name='accident',
            name='ARR_HOUR',
            field=models.CharField(choices=[('0', '0\u65f6'), ('1', '1\u65f6'), ('2', '2\u65f6'), ('3', '3\u65f6'), ('4', '4\u65f6'), ('5', '5\u65f6'), ('6', '6\u65f6'), ('7', '7\u65f6'), ('8', '8\u65f6'), ('9', '9\u65f6'), ('10', '10\u65f6'), ('11', '11\u65f6'), ('12', '12\u65f6'), ('13', '13\u65f6'), ('14', '14\u65f6'), ('15', '15\u65f6'), ('16', '16\u65f6'), ('17', '17\u65f6'), ('18', '18\u65f6'), ('19', '19\u65f6'), ('20', '20\u65f6'), ('21', '21\u65f6'), ('22', '22\u65f6'), ('23', '23\u65f6'), ('88', '\u672a\u6709'), ('99', '\u672a\u77e5')], default=99, help_text='\u533b\u7597\u670d\u52a1\u5230\u8fbe\u5c0f\u65f6\u6570', max_length=10),
        ),
    ]
