# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-02 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrash', '0021_auto_20180201_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicledata',
            name='DR_SF1',
            field=models.CharField(choices=[('0', '\u65e0/\u4e0d\u9002\u7528'), ('1', '\u7c97\u5fc3\u9a7e\u9a76'), ('2', '\u8def\u6012/\u4fb5\u7565\u6027\u7684\u9a7e\u9a76'), ('3', '\u80ce\u513f\u6b7b\u4ea1/\u51fa\u751f\u7684\u6bcd\u4eb2'), ('4', '\u5ea7\u6905\u9760\u80cc\u4e0d\u6070\u5f53-\u659c\u8eba'), ('5', '\u8b66\u5bdf\u6216\u6267\u6cd5\u4eba\u5458'), ('6', '\u5728\u7981\u6b62\u7684\u9053\u8def\u9a7e\u9a76'), ('7', '\u7528\u6263\u7559\u6216\u540a\u9500\u7684\u9a7e\u7167\u9a7e\u9a76'), ('8', '\u7559\u4e0b\u53d1\u52a8\u673a\u8fd0\u884c\u4f46\u65e0\u4eba\u770b\u5b88\u7684\u8f66\u8f86'), ('9', '\u4e58\u5ba2\u6216\u8d27\u7269\u8d85\u8f7d\u6216\u88c5\u8f7d\u4e0d\u5f53'), ('10', '\u4e0d\u6b63\u5f53\u63a8\u8f66\u6216\u62d6\u8f66'), ('11', '\u672a\u5f00\u706f\u6216\u672a\u53ca\u65f6\u5f00\u706f'), ('12', '\u64cd\u4f5c\u4e0d\u9700\u8981\u7684\u8bbe\u5907'), ('13', '\u9519\u8bef\u6216\u4e0d\u5408\u7406\u7684\u53d8\u9053'), ('14', '\u672a\u80fd\u4fdd\u6301\u6b63\u786e\u7684\u8f66\u9053'), ('15', '\u6545\u610f\u5728\u8def\u80a9\u4e0a\u3001\u6c9f\u6e20\u6216\u4eba\u884c\u9053\u4e0a\u975e\u6cd5\u9a7e\u9a76'), ('16', '\u4e0d\u6070\u5f53\u5730\u8fdb\u5165\u6216\u9000\u51fa\u4ea4\u901a\u8def\u53e3'), ('17', '\u4e0d\u6070\u5f53\u5730\u542f\u52a8\u6216\u5012\u8f66'), ('18', '\u5728\u9519\u8bef\u7684\u4e00\u4fa7\u901a\u884c'), ('19', '\u901a\u8fc7\u8ddd\u79bb\u4e0d\u8db3\u7684\u5730\u65b9/\u89c6\u91ce\u4e0d\u8db3/\u8d85\u8f66\u65f6\u672a\u80fd\u907f\u8ba9'), ('20', '\u4ee5\u9519\u8bef\u3001\u9c81\u83bd\u3001\u7c97\u5fc3\u7684\u65b9\u5f0f\u64cd\u4f5c\u8f66\u8f86'), ('21', '\u672a\u80fd\u907f\u8ba9\u9053\u8def\u53f3\u4fa7'), ('22', '\u8ffd\u6355\u4e2d\u7684\u8b66\u5bdf'), ('23', '\u4e0d\u9075\u5b88\u4ea4\u901a\u6807\u5fd7\uff0c\u4ea4\u901a\u7ba1\u5236\u7684\u8bbe\u5907\u6216\u4ea4\u8b66\uff0c\u4e0d\u9075\u5b88\u4ea4\u89c4'), ('24', '\u7a7f\u8fc7\u6216\u7ed5\u8fc7\u5c4f\u969c'), ('25', '\u5de6\u8f6c\u8f66\u9053\u53f3\u8f6c\uff1b\u53f3\u8f6c\u8f66\u9053\u5de6\u8f6c'), ('26', '\u7f3a\u4e4f\u64cd\u4f5c\u7ecf\u9a8c'), ('27', '\u4e0d\u719f\u6089\u9053\u8def'), ('28', '\u77eb\u6b63\u8fc7\u5ea6'), ('29', '\u4e25\u91cd\u9006\u98ce'), ('30', '\u6765\u81ea\u5361\u8f66\u7684\u98ce'), ('31', '\u6ed1\u6e9c\u6216\u677e\u6563\u7684\u8868\u9762'), ('32', '\u8f6e\u80ce\u7206\u7834\u6216\u6f0f\u6c14'), ('33', '\u672a\u6ce8\u610f\u5230\u524d\u65b9\u7269\u4f53/\u884c\u4eba'), ('99', '\u672a\u77e5')], default='0', help_text='\u8be5\u5143\u7d20\u8868\u793a\u4e0e\u9a7e\u9a76\u5458\u76f8\u5173\u7684\u56e0\u7d20\uff0c\u6700\u591a4\u9879', max_length=30),
        ),
        migrations.AlterField(
            model_name='vehicledata',
            name='DR_SF2',
            field=models.CharField(choices=[('0', '\u65e0/\u4e0d\u9002\u7528'), ('1', '\u7c97\u5fc3\u9a7e\u9a76'), ('2', '\u8def\u6012/\u4fb5\u7565\u6027\u7684\u9a7e\u9a76'), ('3', '\u80ce\u513f\u6b7b\u4ea1/\u51fa\u751f\u7684\u6bcd\u4eb2'), ('4', '\u5ea7\u6905\u9760\u80cc\u4e0d\u6070\u5f53-\u659c\u8eba'), ('5', '\u8b66\u5bdf\u6216\u6267\u6cd5\u4eba\u5458'), ('6', '\u5728\u7981\u6b62\u7684\u9053\u8def\u9a7e\u9a76'), ('7', '\u7528\u6263\u7559\u6216\u540a\u9500\u7684\u9a7e\u7167\u9a7e\u9a76'), ('8', '\u7559\u4e0b\u53d1\u52a8\u673a\u8fd0\u884c\u4f46\u65e0\u4eba\u770b\u5b88\u7684\u8f66\u8f86'), ('9', '\u4e58\u5ba2\u6216\u8d27\u7269\u8d85\u8f7d\u6216\u88c5\u8f7d\u4e0d\u5f53'), ('10', '\u4e0d\u6b63\u5f53\u63a8\u8f66\u6216\u62d6\u8f66'), ('11', '\u672a\u5f00\u706f\u6216\u672a\u53ca\u65f6\u5f00\u706f'), ('12', '\u64cd\u4f5c\u4e0d\u9700\u8981\u7684\u8bbe\u5907'), ('13', '\u9519\u8bef\u6216\u4e0d\u5408\u7406\u7684\u53d8\u9053'), ('14', '\u672a\u80fd\u4fdd\u6301\u6b63\u786e\u7684\u8f66\u9053'), ('15', '\u6545\u610f\u5728\u8def\u80a9\u4e0a\u3001\u6c9f\u6e20\u6216\u4eba\u884c\u9053\u4e0a\u975e\u6cd5\u9a7e\u9a76'), ('16', '\u4e0d\u6070\u5f53\u5730\u8fdb\u5165\u6216\u9000\u51fa\u4ea4\u901a\u8def\u53e3'), ('17', '\u4e0d\u6070\u5f53\u5730\u542f\u52a8\u6216\u5012\u8f66'), ('18', '\u5728\u9519\u8bef\u7684\u4e00\u4fa7\u901a\u884c'), ('19', '\u901a\u8fc7\u8ddd\u79bb\u4e0d\u8db3\u7684\u5730\u65b9/\u89c6\u91ce\u4e0d\u8db3/\u8d85\u8f66\u65f6\u672a\u80fd\u907f\u8ba9'), ('20', '\u4ee5\u9519\u8bef\u3001\u9c81\u83bd\u3001\u7c97\u5fc3\u7684\u65b9\u5f0f\u64cd\u4f5c\u8f66\u8f86'), ('21', '\u672a\u80fd\u907f\u8ba9\u9053\u8def\u53f3\u4fa7'), ('22', '\u8ffd\u6355\u4e2d\u7684\u8b66\u5bdf'), ('23', '\u4e0d\u9075\u5b88\u4ea4\u901a\u6807\u5fd7\uff0c\u4ea4\u901a\u7ba1\u5236\u7684\u8bbe\u5907\u6216\u4ea4\u8b66\uff0c\u4e0d\u9075\u5b88\u4ea4\u89c4'), ('24', '\u7a7f\u8fc7\u6216\u7ed5\u8fc7\u5c4f\u969c'), ('25', '\u5de6\u8f6c\u8f66\u9053\u53f3\u8f6c\uff1b\u53f3\u8f6c\u8f66\u9053\u5de6\u8f6c'), ('26', '\u7f3a\u4e4f\u64cd\u4f5c\u7ecf\u9a8c'), ('27', '\u4e0d\u719f\u6089\u9053\u8def'), ('28', '\u77eb\u6b63\u8fc7\u5ea6'), ('29', '\u4e25\u91cd\u9006\u98ce'), ('30', '\u6765\u81ea\u5361\u8f66\u7684\u98ce'), ('31', '\u6ed1\u6e9c\u6216\u677e\u6563\u7684\u8868\u9762'), ('32', '\u8f6e\u80ce\u7206\u7834\u6216\u6f0f\u6c14'), ('33', '\u672a\u6ce8\u610f\u5230\u524d\u65b9\u7269\u4f53/\u884c\u4eba'), ('99', '\u672a\u77e5')], default='0', help_text='\u8be5\u5143\u7d20\u8868\u793a\u4e0e\u9a7e\u9a76\u5458\u76f8\u5173\u7684\u56e0\u7d20\uff0c\u6700\u591a4\u9879', max_length=30),
        ),
        migrations.AlterField(
            model_name='vehicledata',
            name='DR_SF3',
            field=models.CharField(choices=[('0', '\u65e0/\u4e0d\u9002\u7528'), ('1', '\u7c97\u5fc3\u9a7e\u9a76'), ('2', '\u8def\u6012/\u4fb5\u7565\u6027\u7684\u9a7e\u9a76'), ('3', '\u80ce\u513f\u6b7b\u4ea1/\u51fa\u751f\u7684\u6bcd\u4eb2'), ('4', '\u5ea7\u6905\u9760\u80cc\u4e0d\u6070\u5f53-\u659c\u8eba'), ('5', '\u8b66\u5bdf\u6216\u6267\u6cd5\u4eba\u5458'), ('6', '\u5728\u7981\u6b62\u7684\u9053\u8def\u9a7e\u9a76'), ('7', '\u7528\u6263\u7559\u6216\u540a\u9500\u7684\u9a7e\u7167\u9a7e\u9a76'), ('8', '\u7559\u4e0b\u53d1\u52a8\u673a\u8fd0\u884c\u4f46\u65e0\u4eba\u770b\u5b88\u7684\u8f66\u8f86'), ('9', '\u4e58\u5ba2\u6216\u8d27\u7269\u8d85\u8f7d\u6216\u88c5\u8f7d\u4e0d\u5f53'), ('10', '\u4e0d\u6b63\u5f53\u63a8\u8f66\u6216\u62d6\u8f66'), ('11', '\u672a\u5f00\u706f\u6216\u672a\u53ca\u65f6\u5f00\u706f'), ('12', '\u64cd\u4f5c\u4e0d\u9700\u8981\u7684\u8bbe\u5907'), ('13', '\u9519\u8bef\u6216\u4e0d\u5408\u7406\u7684\u53d8\u9053'), ('14', '\u672a\u80fd\u4fdd\u6301\u6b63\u786e\u7684\u8f66\u9053'), ('15', '\u6545\u610f\u5728\u8def\u80a9\u4e0a\u3001\u6c9f\u6e20\u6216\u4eba\u884c\u9053\u4e0a\u975e\u6cd5\u9a7e\u9a76'), ('16', '\u4e0d\u6070\u5f53\u5730\u8fdb\u5165\u6216\u9000\u51fa\u4ea4\u901a\u8def\u53e3'), ('17', '\u4e0d\u6070\u5f53\u5730\u542f\u52a8\u6216\u5012\u8f66'), ('18', '\u5728\u9519\u8bef\u7684\u4e00\u4fa7\u901a\u884c'), ('19', '\u901a\u8fc7\u8ddd\u79bb\u4e0d\u8db3\u7684\u5730\u65b9/\u89c6\u91ce\u4e0d\u8db3/\u8d85\u8f66\u65f6\u672a\u80fd\u907f\u8ba9'), ('20', '\u4ee5\u9519\u8bef\u3001\u9c81\u83bd\u3001\u7c97\u5fc3\u7684\u65b9\u5f0f\u64cd\u4f5c\u8f66\u8f86'), ('21', '\u672a\u80fd\u907f\u8ba9\u9053\u8def\u53f3\u4fa7'), ('22', '\u8ffd\u6355\u4e2d\u7684\u8b66\u5bdf'), ('23', '\u4e0d\u9075\u5b88\u4ea4\u901a\u6807\u5fd7\uff0c\u4ea4\u901a\u7ba1\u5236\u7684\u8bbe\u5907\u6216\u4ea4\u8b66\uff0c\u4e0d\u9075\u5b88\u4ea4\u89c4'), ('24', '\u7a7f\u8fc7\u6216\u7ed5\u8fc7\u5c4f\u969c'), ('25', '\u5de6\u8f6c\u8f66\u9053\u53f3\u8f6c\uff1b\u53f3\u8f6c\u8f66\u9053\u5de6\u8f6c'), ('26', '\u7f3a\u4e4f\u64cd\u4f5c\u7ecf\u9a8c'), ('27', '\u4e0d\u719f\u6089\u9053\u8def'), ('28', '\u77eb\u6b63\u8fc7\u5ea6'), ('29', '\u4e25\u91cd\u9006\u98ce'), ('30', '\u6765\u81ea\u5361\u8f66\u7684\u98ce'), ('31', '\u6ed1\u6e9c\u6216\u677e\u6563\u7684\u8868\u9762'), ('32', '\u8f6e\u80ce\u7206\u7834\u6216\u6f0f\u6c14'), ('33', '\u672a\u6ce8\u610f\u5230\u524d\u65b9\u7269\u4f53/\u884c\u4eba'), ('99', '\u672a\u77e5')], default='0', help_text='\u8be5\u5143\u7d20\u8868\u793a\u4e0e\u9a7e\u9a76\u5458\u76f8\u5173\u7684\u56e0\u7d20\uff0c\u6700\u591a4\u9879', max_length=30),
        ),
        migrations.AlterField(
            model_name='vehicledata',
            name='DR_SF4',
            field=models.CharField(choices=[('0', '\u65e0/\u4e0d\u9002\u7528'), ('1', '\u7c97\u5fc3\u9a7e\u9a76'), ('2', '\u8def\u6012/\u4fb5\u7565\u6027\u7684\u9a7e\u9a76'), ('3', '\u80ce\u513f\u6b7b\u4ea1/\u51fa\u751f\u7684\u6bcd\u4eb2'), ('4', '\u5ea7\u6905\u9760\u80cc\u4e0d\u6070\u5f53-\u659c\u8eba'), ('5', '\u8b66\u5bdf\u6216\u6267\u6cd5\u4eba\u5458'), ('6', '\u5728\u7981\u6b62\u7684\u9053\u8def\u9a7e\u9a76'), ('7', '\u7528\u6263\u7559\u6216\u540a\u9500\u7684\u9a7e\u7167\u9a7e\u9a76'), ('8', '\u7559\u4e0b\u53d1\u52a8\u673a\u8fd0\u884c\u4f46\u65e0\u4eba\u770b\u5b88\u7684\u8f66\u8f86'), ('9', '\u4e58\u5ba2\u6216\u8d27\u7269\u8d85\u8f7d\u6216\u88c5\u8f7d\u4e0d\u5f53'), ('10', '\u4e0d\u6b63\u5f53\u63a8\u8f66\u6216\u62d6\u8f66'), ('11', '\u672a\u5f00\u706f\u6216\u672a\u53ca\u65f6\u5f00\u706f'), ('12', '\u64cd\u4f5c\u4e0d\u9700\u8981\u7684\u8bbe\u5907'), ('13', '\u9519\u8bef\u6216\u4e0d\u5408\u7406\u7684\u53d8\u9053'), ('14', '\u672a\u80fd\u4fdd\u6301\u6b63\u786e\u7684\u8f66\u9053'), ('15', '\u6545\u610f\u5728\u8def\u80a9\u4e0a\u3001\u6c9f\u6e20\u6216\u4eba\u884c\u9053\u4e0a\u975e\u6cd5\u9a7e\u9a76'), ('16', '\u4e0d\u6070\u5f53\u5730\u8fdb\u5165\u6216\u9000\u51fa\u4ea4\u901a\u8def\u53e3'), ('17', '\u4e0d\u6070\u5f53\u5730\u542f\u52a8\u6216\u5012\u8f66'), ('18', '\u5728\u9519\u8bef\u7684\u4e00\u4fa7\u901a\u884c'), ('19', '\u901a\u8fc7\u8ddd\u79bb\u4e0d\u8db3\u7684\u5730\u65b9/\u89c6\u91ce\u4e0d\u8db3/\u8d85\u8f66\u65f6\u672a\u80fd\u907f\u8ba9'), ('20', '\u4ee5\u9519\u8bef\u3001\u9c81\u83bd\u3001\u7c97\u5fc3\u7684\u65b9\u5f0f\u64cd\u4f5c\u8f66\u8f86'), ('21', '\u672a\u80fd\u907f\u8ba9\u9053\u8def\u53f3\u4fa7'), ('22', '\u8ffd\u6355\u4e2d\u7684\u8b66\u5bdf'), ('23', '\u4e0d\u9075\u5b88\u4ea4\u901a\u6807\u5fd7\uff0c\u4ea4\u901a\u7ba1\u5236\u7684\u8bbe\u5907\u6216\u4ea4\u8b66\uff0c\u4e0d\u9075\u5b88\u4ea4\u89c4'), ('24', '\u7a7f\u8fc7\u6216\u7ed5\u8fc7\u5c4f\u969c'), ('25', '\u5de6\u8f6c\u8f66\u9053\u53f3\u8f6c\uff1b\u53f3\u8f6c\u8f66\u9053\u5de6\u8f6c'), ('26', '\u7f3a\u4e4f\u64cd\u4f5c\u7ecf\u9a8c'), ('27', '\u4e0d\u719f\u6089\u9053\u8def'), ('28', '\u77eb\u6b63\u8fc7\u5ea6'), ('29', '\u4e25\u91cd\u9006\u98ce'), ('30', '\u6765\u81ea\u5361\u8f66\u7684\u98ce'), ('31', '\u6ed1\u6e9c\u6216\u677e\u6563\u7684\u8868\u9762'), ('32', '\u8f6e\u80ce\u7206\u7834\u6216\u6f0f\u6c14'), ('33', '\u672a\u6ce8\u610f\u5230\u524d\u65b9\u7269\u4f53/\u884c\u4eba'), ('99', '\u672a\u77e5')], default='0', help_text='\u8be5\u5143\u7d20\u8868\u793a\u4e0e\u9a7e\u9a76\u5458\u76f8\u5173\u7684\u56e0\u7d20\uff0c\u6700\u591a4\u9879', max_length=30),
        ),
    ]
