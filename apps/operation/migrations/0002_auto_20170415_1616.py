# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-15 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursecomments',
            options={'verbose_name': '\u8bfe\u7a0b\u8bc4\u8bba', 'verbose_name_plural': '\u8bfe\u7a0b\u8bc4\u8bba'},
        ),
        migrations.AlterModelOptions(
            name='userask',
            options={'verbose_name': '\u7528\u6237\u54a8\u8be2', 'verbose_name_plural': '\u7528\u6237\u54a8\u8be2'},
        ),
        migrations.AlterModelOptions(
            name='usercourse',
            options={'verbose_name': '\u7528\u6237\u8bfe\u7a0b', 'verbose_name_plural': '\u7528\u6237\u8bfe\u7a0b'},
        ),
        migrations.AlterModelOptions(
            name='userfavorite',
            options={'verbose_name': '\u7528\u6237\u6536\u85cf', 'verbose_name_plural': '\u7528\u6237\u6536\u85cf'},
        ),
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': '\u7528\u6237\u6d88\u606f', 'verbose_name_plural': '\u7528\u6237\u6d88\u606f'},
        ),
    ]