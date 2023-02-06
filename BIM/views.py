from django.shortcuts import render
from django.views.generic import TemplateView

from common.views import CommonMixin


# Create your views here.
class BIMMainView(CommonMixin, TemplateView):
    title = 'Лаборатория BIM'
    template_name = 'BIM/BIM_index.html'
