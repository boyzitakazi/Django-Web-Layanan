from user_profile.models import UserProfile
from adminapp.models import RegisterKtpModel
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

# Form untuk pengisihal profile
class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image', 'bio', 'location')


# Untuk menampilkan detail profile
class UserDetailModelForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name',)


# Form untuk menampilkan registrasi KTP
class UserRegisterKtpForm(forms.ModelForm):
	class Meta:
		model = RegisterKtpModel
		fields = ('namleng', 'nik', 'no_hp', 'kk', 'akta')


# Untuk menampilkan status proses dan Pesan pada user
class UserStatus(forms.ModelForm):
    class Meta:
        model = RegisterKtpModel
        fields = ('status_proses','pesan')


