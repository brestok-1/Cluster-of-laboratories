from django.urls import path

from laboratories.views import *

app_name = 'laboratories'

urlpatterns = [
    path('<slug:about_slug>', AboutLabView.as_view(), name='students')
]
