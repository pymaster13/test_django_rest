from django.urls import path

from .views import DepartmentListView


urlpatterns = [
    path('all/', DepartmentListView.as_view(), name='departments_set'), 
]

