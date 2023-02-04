from django.shortcuts import render
from django.views.generic import TemplateView

from common.views import CommonMixin


# Create your views here.
class RoboticsMainView(CommonMixin, TemplateView):
    template_name = 'robotics/robotics_index.html'
    title = 'Лаборатория робототехники'


