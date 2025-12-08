from django.shortcuts import get_object_or_404
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

@api_view(['GET','DELETE','PUT','PATCH'])
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'GET':
        taskserializer = TaskSerializer(task)
        return Response(taskserializer.data, status=200)
    
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=204)
    
    elif request.method == 'PUT':
        taskserializer = TaskSerializer(instance=task, data = request.data)
        if taskserializer.is_valid():
            taskserializer.save()
            return Response(taskserializer.data, status= 200)
        return Response(taskserializer.errors, status=400)
    
    elif request.method == 'PATCH':
        taskserializer = TaskSerializer(instance=task, data = request.data, partial=True)
        if taskserializer.is_valid():
            taskserializer.save()
            return Response(taskserializer.data, status= 200)
        return Response(taskserializer.errors, status=400)