from django.urls import path

from robotics.views import *

app_name = 'robotics'

urlpatterns = [
    path('', RoboticsMainView.as_view(), name='index'),
    path('technologies/<slug:tech_slug>', RoboticsTechnologyView.as_view(), name='tech'),
    path('projects/<slug:project_slug>', RoboticsProjectsView.as_view(), name='project'),
]
