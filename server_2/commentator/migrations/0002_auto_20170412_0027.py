# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentator',
            name='previuosly_provided_commentary',
        ),
        migrations.AddField(
            model_name='commentator',
            name='name',
            field=models.CharField(default='admin', max_length=100),
        ),
    ]
