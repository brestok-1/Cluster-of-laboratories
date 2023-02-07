from django.shortcuts import render
from django.views.generic import TemplateView

from common.views import CommonMixin


# Create your views here.

class TechnicalVisionMainView(CommonMixin, TemplateView):
    template_name = 'technical_vision/vision_index.html'
    title = "Лаборатория Технического Зрения"

