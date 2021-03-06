# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-01 16:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20180301_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='points',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([('user', 'content')]),
        ),
    ]
