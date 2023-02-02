from django.urls import path

from cluster.views import OneNewView

app_name = 'cluster'

urlpatterns = [
    path('news/<slug:new_slug>', OneNewView.as_view(), name='one_new'),
]
