from django.urls import path

from robotics.views import RoboticsMainView, BIMMainView, TechnicalVisionView, AgricultureView, TechnologyView, \
    ProjectsView, CourseView, ListProjects

app_name = 'robotics'

urlpatterns = [
    path('robotics/', RoboticsMainView.as_view(), name='robotics'),
    path('BIM/', BIMMainView.as_view(), name='BIM'),
    path('technical-vision/', TechnicalVisionView.as_view(), name='technical_vision'),
    path('agriculture/', AgricultureView.as_view(), name='agriculture'),
    path('technologies/<slug:tech_slug>', TechnologyView.as_view(), name='tech'),
    path('projects/<slug:project_slug>', ProjectsView.as_view(), name='project'),
    path('courses/<slug:course_slug>', CourseView.as_view(), name='course'),
    path('projects/', ListProjects.as_view(), name='list_projects'),
]
