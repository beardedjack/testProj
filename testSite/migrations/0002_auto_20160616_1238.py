# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]