# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-06 04:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0019_auto_20200205_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerktpmodel',
            name='status_proses',
            field=models.CharField(choices=[('Belum Diproses', 'Belum Diproses'), ('Sedang Diproses', 'Sedang Diproses'), ('Selesai', 'Selesai')], max_length=20),
        ),
    ]
