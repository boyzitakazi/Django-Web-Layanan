# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-03 13:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0016_auto_20200202_0939'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegisterKtpModel',
        ),
    ]