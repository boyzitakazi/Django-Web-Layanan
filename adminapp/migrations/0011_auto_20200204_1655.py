# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-04 16:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_auto_20200204_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perpanjangktpmodel',
            old_name='last_name',
            new_name='nama_belakang',
        ),
        migrations.RenameField(
            model_name='perpanjangktpmodel',
            old_name='first_name',
            new_name='nama_depan',
        ),
        migrations.RenameField(
            model_name='perpanjangktpmodel',
            old_name='no_hp',
            new_name='no_handphone',
        ),
        migrations.RenameField(
            model_name='perpanjangktpmodel',
            old_name='status_proses',
            new_name='status_perpanjang',
        ),
    ]