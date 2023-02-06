from django.urls import path

from BIM.views import *

app_name = 'BIM'

urlpatterns = [
    path('', BIMMainView.as_view(), name='index')
]
