# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-06 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0015_auto_20200205_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerktpmodel',
            name='namleng',
            field=models.CharField(default=None, max_length=30, verbose_name='Nama Lengkap'),
        ),
    ]