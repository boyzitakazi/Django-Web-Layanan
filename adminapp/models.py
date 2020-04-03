# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RegisterKtpModel(models.Model):
    namleng = models.CharField(max_length=30, null=True, blank=True, default=None, verbose_name="Nama Lengkap")
    no_hp = models.IntegerField(null=True, blank=True, default=None, verbose_name="No. Handphone Aktif")
    nik = models.IntegerField(null=True, blank=True, default=None, verbose_name="Nomor Induk Keluarga")
    kk = models.FileField(upload_to="Data_Pemohon/registrasi/", verbose_name="Foto KK", blank=True, max_length=100)
    akta = models.FileField(upload_to="Data_Pemohon/registrasi/", verbose_name="Foto Akta Kelahiran", blank=True, max_length=100)

    STATUS_PROSES = [
    	('Belum Diproses', 'Belum Diproses'),
    	('Sedang Diproses', 'Sedang Diproses'),
    	('Selesai', 'Selesai'),
    ]

# Untuk Status Proses User
    status_proses = models.CharField(
    	max_length=20,
    	choices=STATUS_PROSES,
        default='Belum Proses'
    	)

    pesan = models.TextField(max_length=255, null=True, blank=True, default=None, verbose_name="Pesan")
    
    def __str__(self):
        return "{}. {}. {}".format(self.id, self.namleng, self.nik)
