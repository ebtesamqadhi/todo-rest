from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Task
from .serializer import TaskSerializer
# Create your views here.

@api_view(['GET','POST'])
def task_get(request):
    if request.method == 'POST':
        taskserializer = TaskSerializer(data = request.data)
        if taskserializer.is_valid():
            taskserializer.save()
            return Response(taskserializer.data, status=201) 
        return Response(taskserializer.errors, status=400)
               
    elif request.method == 'GET':
        tasks = Task.objects.all()
        taskserializer = TaskSerializer(tasks, many=True)
        data = {
            "count": tasks.count(),
            "tasks": taskserializer.data
        }
        return Response(data, status=200)
