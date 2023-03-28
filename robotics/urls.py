from django.urls import path

from robotics.views import RoboticsMainView, BIMMainView, TechnicalVisionView, AgricultureView, ListProjectsView, \
    ListTechnologiesView, ListCoursesView, ProjectDetailView, TechnologyDetailView, CourseDetailView

app_name = 'robotics'

urlpatterns = [
    path('robotics/', RoboticsMainView.as_view(), name='robotics'),
    path('BIM/', BIMMainView.as_view(), name='BIM'),
    path('technical-vision/', TechnicalVisionView.as_view(), name='technical_vision'),
    path('agriculture/', AgricultureView.as_view(), name='agriculture'),
    path('projects/<slug:laboratory>/', ListProjectsView.as_view(), name='list_projects'),
    path('technologies/<slug:laboratory>/', ListTechnologiesView.as_view(), name='list_technologies'),
    path('courses/<slug:laboratory>/', ListCoursesView.as_view(), name='list_courses'),
    path('projects/<slug:laboratory>/<slug:project_slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('technologies/<slug:laboratory>/<slug:tech_slug>/', TechnologyDetailView.as_view(), name='tech_detail'),
    path('courses/<slug:laboratory>/<slug:course_slug>/', CourseDetailView.as_view(), name='course_detail'),
]
