# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-02 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180301_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='points',
            field=models.IntegerField(default=1),
        ),
    ]
