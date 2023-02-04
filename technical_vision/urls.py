from django.urls import path

from technical_vision.views import *

app_name = 'technical_vision'

urlpatterns = [
    path('', TechnicalVisionMainView.as_view(), name='index')
]
