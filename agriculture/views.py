from django.shortcuts import render
from django.views.generic import TemplateView

from common.views import CommonMixin


# Create your views here.
class AgricultureMainView(CommonMixin, TemplateView):
    title = 'Лаборатория Точного Земледелия'
    template_name = 'agriculture/index.html'