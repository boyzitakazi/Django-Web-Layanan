from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="homepage"),
    url(r'^terms$', views.TermsView.as_view(), name="terms"),
    url(r'^news$', views.NewsView.as_view(), name="news"),
    url(r'^produk$', views.ProdukDesa.as_view(), name="produk_desa"),
]
