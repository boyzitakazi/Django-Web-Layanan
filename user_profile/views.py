from django.http import HttpResponse
from adminapp.models import RegisterKtpModel
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect, reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from user_profile.forms import UserProfileModelForm, UserDetailModelForm, UserRegisterKtpForm


# Create your views here.

# Untuk menampilkan Akun Profile
class UserProfileView(TemplateView, LoginRequiredMixin):
    
    # template untuk user profile
    template_name = "user_profile/profile_user_form.html"

    def post(self, request, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user_profile_form'] = user_profile_form = UserProfileModelForm(request.POST, request.FILES,
                                                                                instance=request.user.user_profile)
        context['user_detail_form'] = user_detail_form = UserDetailModelForm(request.POST,
                                                                             instance=request.user)
        if user_profile_form.is_valid() and  user_detail_form.is_valid():
            user_profile_form.save()
            user_detail_form.save()
            return redirect(reverse('profile'))
        else:
            print(user_profile_form.errors, "++++++")

        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user_profile_form'] = UserProfileModelForm(instance=request.user.user_profile)
        context['user_detail_form'] = UserDetailModelForm(instance=request.user)
        return render(request, self.template_name, context=context)


# Untuk Status Proses Pada User
def index(request):

    # Form untuk menampilkan semua data user
    post_model = RegisterKtpModel.objects.all()
    template_name = 'user_profile/profile.html'

    context = {
        'heading':'Home Pages',
        'post_model':post_model,
    }

    return render(request, template_name, context)


# Untuk User Registrasi KTP
def UserRegisterKtp(request):

    # Form untuk pengisian KTP
    akun_form = UserRegisterKtpForm(request.POST or None, request.FILES)

    if request.user.is_authenticated():
        if request.method == 'POST':
            if akun_form.is_valid():
                akun_form.save()
                print(request.session.get('user.id'))

                return redirect('status_ktp')
    else:
        print(akun_form.errors, "++++++")

    context = {
        "page_title":"Tambah akun",
        "akun_form":akun_form,
    }

    return render(request,'user_profile/register_ktp.html',context)


# Untuk Menampilkan Pesan Setelah Registrasi
class Status(TemplateView):
    template_name = "user_profile/registered_ktp.html"


# Untuk Menampilkan Pesan Setelah Registrasi
class Panduan(TemplateView):
    template_name = "user_profile/panduan/panduan.html"


# Untuk menampilkan data berdasarkan user
def only_post_user(request, post_user):

    # Form untuk menampilkan semua data user
    post_model = RegisterKtpModel.objects.filter(id=post_user)
    template_name = 'user_profile/profile.html'

    context = {
        'heading':'Home Pages',
        'post_model':post_model,
    }

    return render(request, template_name, context)
