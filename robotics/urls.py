from django.urls import path

from robotics.views import *

app_name = 'robotics'

urlpatterns = [
    path('', RoboticsMainView.as_view(), name='index')
]
