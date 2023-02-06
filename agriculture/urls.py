from django.urls import path

from agriculture.views import *

app_name = 'agriculture'

urlpatterns = [
    path('', AgricultureMainView.as_view(), name='index')
]
