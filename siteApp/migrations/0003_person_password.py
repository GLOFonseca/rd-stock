# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0002_auto_20170611_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
