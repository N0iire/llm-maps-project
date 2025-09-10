# maps_api/urls.py

from django.urls import path
from .views import FindPlaceAPIView, TaskStatusAPIView

urlpatterns = [
    path('find-place/', FindPlaceAPIView.as_view(), name='find-place'),
    path('task-status/<str:task_id>/', TaskStatusAPIView.as_view(), name='task-status'),
]