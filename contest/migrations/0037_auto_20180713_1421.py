# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0036_auto_20180712_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='allowed_lang',
            field=models.CharField(default='c,cc14,cc17,cpp,cs,hs,java,js,ocaml,pas,perl,php,py2,pypy,pypy3,python,rs,scala,scipy,text', max_length=192, verbose_name='Allowed languages'),
        ),
    ]
