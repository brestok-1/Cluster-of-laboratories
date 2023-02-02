from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView

from common.views import CommonMixin

from .models import *


class IndexView(CommonMixin, ListView):
    template_name = 'cluster/index.html'
    title = 'Добро пожаловать на наш кластер'

    def get_queryset(self):
        return News.objects.all()[:5]


class NewsView(CommonMixin, ListView):
    title = 'Новости'
    template_name = 'cluster/news.html'

    def get_queryset(self):
        return News.objects.all()[:5]