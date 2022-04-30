from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.models import Product

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname'] = "Babayew Eziz"
        context['product_list'] = Product.objects.all()
        return context


class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(TemplateView):
    template_name = "contact.html"