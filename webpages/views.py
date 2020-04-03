from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = "webpages/homepage.html"

class TermsView(TemplateView):
    template_name = "webpages/terms.html"

class NewsView(TemplateView):
    template_name = "webpages/news.html"

class ProdukDesa(TemplateView):
    template_name = "webpages/produk_desa.html"
