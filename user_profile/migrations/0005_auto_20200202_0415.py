# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-02 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_registerktpmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerktpmodel',
            name='document',
            field=models.FileField(blank=True, default=None, null=True, upload_to=b'Data_Pemohon'),
        ),
        migrations.AlterField(
            model_name='registerktpmodel',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='registerktpmodel',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='registerktpmodel',
            name='nik',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]