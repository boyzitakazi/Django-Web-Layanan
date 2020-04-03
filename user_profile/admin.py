from django.contrib import admin
from user_profile.models import UserProfile
from adminapp.models import RegisterKtpModel
# Register your models here.

# Registrasi UserProfile dari models user_profile
admin.site.register(UserProfile)

# Registrasi UserProfile dari models adminapp
admin.site.register(RegisterKtpModel)


