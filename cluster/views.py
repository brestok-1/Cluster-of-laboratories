from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView, DetailView

from common.views import CommonMixin

from .models import News, Students


class IndexView(CommonMixin, TemplateView):
    template_name = 'cluster/index.html'
    title = 'Добро пожаловать на наш кластер'
    # def get_queryset(self):
    #     return News.objects.all()[:5]


class ListNewsView(CommonMixin, ListView):
    title = 'Новости'
    model = News
    template_name = 'cluster/list_news.html'


class OneNewView(CommonMixin, DetailView):
    template_name = 'cluster/one_new.html'
    slug_url_kwarg = 'new_slug'
    model = News

    def get_context_data(self, **kwargs):
        context = super(OneNewView, self).get_context_data(**kwargs)
        context['title'] = f'Новости - {self.object.title}'
        return context


class StudentsView(CommonMixin, DetailView):
    template_name = 'cluster/student.html'
    model = Students
    slug_url_kwarg = 'student_slug'

    def get_context_data(self, **kwargs):
        context = super(StudentsView, self).get_context_data(**kwargs)
        context['title'] = f'Вопрос : {self.object.title}'
        return context
