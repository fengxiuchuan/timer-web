# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-30 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnav', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tperson',
            name='p_name',
            field=models.CharField(default=None, max_length=50, null=None),
        ),
    ]
