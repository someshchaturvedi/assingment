# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentator', '0002_auto_20170412_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentator',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
