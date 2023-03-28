import re

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from common.views import CommonMixin, LaboratoryMixin, DetailMixin, ListMixin, LaboratoryDataMixin
from robotics.models import *


# Create your views here.
class RoboticsMainView(LaboratoryMixin, TemplateView):
    template_name = 'robotics/robotics_index.html'
    title = 'Лаборатория "Промышленная робототехника"'


class BIMMainView(LaboratoryMixin, TemplateView):
    template_name = 'robotics/BIM_index.html'
    title = 'Лаборатория "Инновации в строительстве"'


class TechnicalVisionView(LaboratoryMixin, TemplateView):
    template_name = 'robotics/technical_vision.html'
    title = 'Лаборатория "Техническое зрение"'


class AgricultureView(LaboratoryMixin, TemplateView):
    template_name = 'robotics/agriculture_index.html'
    title = 'Лаборатория "Цифровой инжиниринг АПК"'


# class TechnologyView(DetailMixin, DetailView):
#     template_name = 'robotics/tech_detail.html'
#     slug_url_kwarg = 'tech_slug'
#     model = Technologies
#
#     def get_context_data(self, **kwargs):
#         context = super(TechnologyView, self).get_context_data(**kwargs)
#         context['title'] = f'Технология - "{self.object.name}"'
#         return context
#

# class ProjectsView(DetailMixin, DetailView):
#     template_name = 'robotics/tech_detail.html'
#     slug_url_kwarg = 'project_slug'
#     model = Projects
#
#     def get_context_data(self, **kwargs):
#         context = super(ProjectsView, self).get_context_data(**kwargs)
#         context['title'] = f'Проект - "{self.object.name}"'
#         return context
#
#
# class CourseView(DetailMixin, DetailView):
#     template_name = 'robotics/course_detail.html'
#     slug_url_kwarg = 'course_slug'
#     model = Courses
#
#     def get_context_data(self, **kwargs):
#         context = super(CourseView, self).get_context_data(**kwargs)
#         context['title'] = f'Курс - "{self.object.name}"'
#         return context


class ListProjectsView(ListMixin, ListView):
    template_name = 'robotics/list_projects.html'
    title = 'Проекты'

    def get_queryset(self):
        return Projects.objects.filter(owner__slug=self.kwargs.get('laboratory'))


class ListTechnologiesView(ListMixin, ListView):
    template_name = 'robotics/list_projects.html'
    title = "Технологии"

    def get_queryset(self):
        return Technologies.objects.filter(owner__slug=self.kwargs.get('laboratory'))


class ListCoursesView(ListMixin, ListView):
    template_name = 'robotics/list_courses.html'
    title = "Курсы"

    def get_queryset(self):
        return Courses.objects.filter(owner__slug=self.kwargs.get('laboratory'))


class ProjectDetailView(LaboratoryDataMixin, DetailView):
    template_name = 'robotics/project_detail.html'
    model = Projects
    slug_url_kwarg = 'project_slug'
    title = 'Проект'


class TechnologyDetailView(LaboratoryDataMixin, DetailView):
    template_name = 'robotics/project_detail.html'
    model = Technologies
    slug_url_kwarg = 'tech_slug'
    title = 'Технология'


class CourseDetailView(LaboratoryDataMixin, DetailView):
    template_name = 'robotics/course_detail.html'
    model = Courses
    slug_url_kwarg = 'course_slug'
    title = 'Курс'
