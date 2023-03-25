from django.urls import path

from robotics.views import RoboticsMainView, BIMMainView, TechnicalVisionView, AgricultureView, ListProjectsView

app_name = 'robotics'

urlpatterns = [
    path('robotics/', RoboticsMainView.as_view(), name='robotics'),
    path('BIM/', BIMMainView.as_view(), name='BIM'),
    path('technical-vision/', TechnicalVisionView.as_view(), name='technical_vision'),
    path('agriculture/', AgricultureView.as_view(), name='agriculture'),
    path('projects/<slug:laboratory>', ListProjectsView.as_view(), name='list_projects'),
]
