# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-02 15:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20180302_1449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-points']},
        ),
    ]