from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from common.views import CommonMixin
from robotics.models import ProjectsRobotics, TechnologiesRobotics, CoursesRobotics


# Create your views here.
class RoboticsMainView(CommonMixin, TemplateView):
    template_name = 'robotics/index.html'
    title = 'Лаборатория робототехники'

    def get_context_data(self, **kwargs):
        context = super(RoboticsMainView, self).get_context_data(**kwargs)
        context['technologies'] = TechnologiesRobotics.objects.all()[:3]
        context['projects'] = ProjectsRobotics.objects.all()[:3]
        context['courses'] = CoursesRobotics.objects.all()[:3]
        return context


class RoboticsTechnologyView(CommonMixin, DetailView):
    template_name = 'robotics/tech_detail.html'
    slug_url_kwarg = 'tech_slug'
    model = TechnologiesRobotics

    def get_context_data(self, **kwargs):
        context = super(RoboticsTechnologyView, self).get_context_data(**kwargs)
        context['technologies'] = TechnologiesRobotics.objects.all()
        context['projects'] = ProjectsRobotics.objects.all()
        context['courses'] = CoursesRobotics.objects.all()
        context['title'] = f'Технология - "{self.object.name}"'
        return context


class RoboticsProjectsView(DetailView):
    template_name = 'robotics/tech_detail.html'
    slug_url_kwarg = 'project_slug'
    model = ProjectsRobotics

    def get_context_data(self, **kwargs):
        context = super(RoboticsProjectsView, self).get_context_data(**kwargs)
        context['technologies'] = TechnologiesRobotics.objects.all()
        context['projects'] = ProjectsRobotics.objects.all()
        context['courses'] = CoursesRobotics.objects.all()
        context['title'] = f'Проект - "{self.object.name}"'
        return context
