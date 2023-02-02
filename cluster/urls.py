from django.urls import path

from cluster.views import OneNewView, ListNewsView

app_name = 'cluster'

urlpatterns = [
    path('news/', ListNewsView.as_view(), name= 'list_news'),
    path('news/<slug:new_slug>', OneNewView.as_view(), name='one_new'),
]
