# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-27 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0015_auto_20170920_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestparticipant',
            name='is_disabled',
            field=models.BooleanField(default=False),
        ),
    ]
