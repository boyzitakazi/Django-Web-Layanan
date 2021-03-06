# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-03 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerktpmodel',
            name='document',
            field=models.FileField(blank=True, upload_to='Data_Pemohon', verbose_name='Upload Berkas'),
        ),
        migrations.AlterField(
            model_name='registerktpmodel',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=30, verbose_name='Nama Depan'),
        ),
        migrations.AlterField(
            model_name='registerktpmodel',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=30, verbose_name='Nama Belakang'),
        ),
    ]
