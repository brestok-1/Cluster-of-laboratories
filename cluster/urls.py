from django.urls import path, include

from cluster.views import OneNewView, ListNewsView, IndexView, StudentsView

app_name = 'cluster'

urlpatterns = [
    path('news/', ListNewsView.as_view(), name='list_news'),
    path('news/<slug:new_slug>', OneNewView.as_view(), name='one_new'),
    path('students/<slug:student_slug>', StudentsView.as_view(), name='students'),
]
