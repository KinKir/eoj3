# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-29 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0007_auto_20170428_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contestparticipant',
            options={'ordering': ['-score', 'penalty']},
        ),
        migrations.AlterField(
            model_name='contestparticipant',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]