# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-06 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0023_auto_20200206_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerktpmodel',
            name='namleng',
            field=models.CharField(blank=True, default=None, max_length=30, verbose_name='Nama Lengkap'),
        ),
        migrations.AlterField(
            model_name='registerktpmodel',
            name='nik',
            field=models.IntegerField(default=None, null=True, verbose_name='Nomor Induk Keluarga'),
        ),
    ]
