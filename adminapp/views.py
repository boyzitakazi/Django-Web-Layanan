# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from adminapp.models import RegisterKtpModel
from user_profile.forms import UserRegisterKtpForm, UserStatus
from django.contrib import messages
from django.views.generic import CreateView


# Create your views here.

# Untuk menampilkan Status Proses Pada User
def statusProses(request,status_id):
	post_model = RegisterKtpModel.objects.get(id=status_id)

	data = {
		'status_proses'	: post_model.status_proses,
	}

	akun_form = UserStatus(request.POST or None, initial=data, instance=post_model)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('admin-dhasboard')

	context = {
		'heading':'Update Data',
		'akun_form':akun_form,
	}	

	return render(request,'user_profile/register_ktp.html',context)



# Untuk Menampilkan Semua Data User
def index(request):
	post_model = RegisterKtpModel.objects.all()
	user_group = Group.objects.get(name='admin')
	user_akun  = request.user.groups.all()

	template_name = None
	if user_group in user_akun:
		# logika untuk super user
		template_name = 'user_profile/profile.html'
		print(request.POST)
	else:
		# logika untuk diluar group
		return redirect('homepage')

	context = {
		'heading':'Home Pages',
		'post_model':post_model,
	}

	
	return render(request, template_name, context)



# Untuk Update Data User
def update(request,update_id):
	post_model = RegisterKtpModel.objects.get(id=update_id)

	data = {
		'namleng'		: post_model.namleng,
		'nik'			: post_model.nik,
		'document'		: post_model.kk,
		'document'		: post_model.akta,
	}

	akun_form = UserRegisterKtpForm(request.POST or None, initial=data, instance=post_model)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('admin-dhasboard')

	context = {
		'heading':'Update Data',
		'akun_form':akun_form,
	}	

	return render(request,'user_profile/register_ktp.html',context)


# Untuk Delete User
def delete(request, delete_id):
	obj = get_object_or_404(RegisterKtpModel, id=delete_id)

	if request.user.is_authenticated():
		if request.method == 'POST':
			obj.delete()
			messages.success(request, 'Data Berhasil Dihapus')

			return redirect('admin-dhasboard')

	context = {
		'object':obj,
	}
	return render(request, 'adminapp/delete_confirm.html', context)

