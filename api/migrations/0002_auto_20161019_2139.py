# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 02:39
from __future__ import unicode_literals

from django.db import migrations, models
import tastypie.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=tastypie.utils.timezone.now, verbose_name=b'date published'),
        ),
    ]
