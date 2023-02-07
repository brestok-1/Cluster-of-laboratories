from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView

from common.views import CommonMixin

from .models import News, Students
from BIM.models import *
from agriculture.models import *
from technical_vision.models import *
from robotics.models import *


class IndexView(CommonMixin, TemplateView):
    template_name = 'cluster/index.html'
    title = 'Добро пожаловать на наш кластер'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        total_arr = list(ProjectsRobotics.objects.all()) + list(
            ProjectsVision.objects.all()) + list(ProjectsAgriculture.objects.all()) + list(ProjectsBIM.objects.all())
        context['projects'] = sorted(total_arr, key=lambda x: x.time_created, reverse=True)[:5]
        return context


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
        context['title'] = f'Новости - {self.object.name}'
        return context


class StudentsView(CommonMixin, DetailView):
    template_name = 'cluster/student.html'
    model = Students
    slug_url_kwarg = 'student_slug'

    def get_context_data(self, **kwargs):
        context = super(StudentsView, self).get_context_data(**kwargs)
        context['title'] = f'Вопрос : {self.object.name}'
        return context


class SearchView(CommonMixin, ListView):
    title = 'Результаты поиска'
    template_name = 'cluster/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            return HttpResponseRedirect(reverse('index'))  # we define on what page user is and redirect to this page
        news_list = list(News.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)))
        technologies_list = list(
            TechnologiesVision.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))) + list(
            TechnologiesRobotics.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))) + list(
            TechnologiesAgriculture.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))) + list(
            TechnologiesBIM.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)))
        projects_list = list(
            ProjectsVision.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))) + list(
            ProjectsRobotics.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))) + list(
            ProjectsAgriculture.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))) + list(
            ProjectsBIM.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)))
        return news_list + technologies_list + projects_list
