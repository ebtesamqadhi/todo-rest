from django.urls import path
from . import views

urlpatterns = [
    path('tasks/',views.task_get, name='tasks'),
    path('tasks/<int:pk>',views.task_detail, name='task_detail')
]