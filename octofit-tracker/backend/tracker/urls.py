from django.urls import path
from . import views

urlpatterns = [
    path('activities/', views.ActivityListCreateView.as_view(), name='activities-list'),
]
