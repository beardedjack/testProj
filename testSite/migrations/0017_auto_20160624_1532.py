# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testSite', '0016_auto_20160624_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.FilePathField(),
        ),
    ]