# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testSite', '0010_good_miniaturefilename'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='miniature',
            field=models.FileField(default='favicon.ico', upload_to=''),
        ),
    ]