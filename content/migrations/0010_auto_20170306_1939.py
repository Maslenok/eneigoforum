# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20170306_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(verbose_name='Активный опрос'),
        ),
    ]
