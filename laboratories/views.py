from django.shortcuts import render
from django.views.generic import DetailView

from laboratories.models import AboutLaboratory


# Create your views here.
class AboutLabView(DetailView):
    model = AboutLaboratory
    slug_url_kwarg = 'about_slug'
    template_name = 'laboratories/laboratoryabout.html'
