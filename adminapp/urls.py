from django.conf.urls import url, include
from . import views


# URL Admin
urlpatterns = [
    url(r'^accounts/admin/$', views.index, name="admin-dhasboard"),
	url(r'^accounts/update/(?P<update_id>[0-9]+)/$', views.update, name='admin-update'),
	url(r'^accounts/delete/(?P<delete_id>[0-9]+)/$', views.delete, name='admin-delete'),
	url(r'^accounts/status_proses/(?P<status_id>[0-9]+)/$', views.statusProses, name='status_proses'),
]
