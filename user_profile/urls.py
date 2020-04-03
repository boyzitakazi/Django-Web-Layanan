from django.conf.urls import url, include
from . import views

# URL USER
urlpatterns = [
    url(r'^accounts/status/$', views.index, name="status"),
    url(r'^accounts/register/$', views.UserRegisterKtp, name="register_ktp"),
    url(r'^accounts/profile/$', views.UserProfileView.as_view(), name="profile"),
    url(r'^accounts/registered/$', views.Status.as_view(), name="status_ktp"),
    url(r'^accounts/panduan/$', views.Panduan.as_view(), name="panduan"),
    url(r'^accounts/onlypost/(?P<post_user>[0-9]+)/$', views.only_post_user, name="post_user"),
]
