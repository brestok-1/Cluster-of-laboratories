import re

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView

from common.views import CommonMixin, ClusterMixin

from .models import News, Students
from robotics.models import *


class IndexView(CommonMixin, ClusterMixin, TemplateView):
    template_name = 'cluster/index.html'
    title = 'Центр Цифровых Технологий'
    left_sidebar_selected = 'Main'


class ListNewsView(CommonMixin, ClusterMixin, ListView):
    title = 'Новости'
    model = News
    template_name = 'cluster/list_news.html'
    left_sidebar_selected = 'News'


class OneNewView(ClusterMixin, DetailView):
    template_name = 'cluster/one_new.html'
    slug_url_kwarg = 'new_slug'
    model = News

    def get_context_data(self, **kwargs):
        context = super(OneNewView, self).get_context_data(**kwargs)
        context['title'] = f'Новости - {self.object.name}'
        return context


class StudentsView(ClusterMixin, DetailView):
    template_name = 'cluster/student.html'
    model = Students
    slug_url_kwarg = 'student_slug'

    def get_context_data(self, **kwargs):
        context = super(StudentsView, self).get_context_data(**kwargs)
        context['title'] = f'Вопрос : {self.object.name}'
        return context


class SearchView(CommonMixin, ClusterMixin, ListView):
    title = 'Результаты поиска'
    template_name = 'cluster/search.html'

    def get(self, *args, **kwargs):
        if re.sub(r' ', '', self.request.GET.get('q')) == '':
            return redirect(self.request.META['HTTP_REFERER'])
        else:
            return super(SearchView, self).get(self, *args, **kwargs)

    def get_queryset(self):
        query = self.request.GET.get('q')
        news_list = list(News.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)))
        projects_list = list(Projects.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)))
        technologies_list = list(
            Technologies.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)))
        return news_list + projects_list + technologies_list


