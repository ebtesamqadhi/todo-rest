from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Task
from .serializer import TaskSerializer
# Create your views here.

@api_view(['GET'])
def task_get(request):
    tasks = Task.objects.all()
    taskserializer = TaskSerializer(tasks, many=True)
    data = {
        "count": tasks.count(),
        "tasks": taskserializer.data
    }
    return Response(data)
