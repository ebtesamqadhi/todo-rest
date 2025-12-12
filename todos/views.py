from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Task
from .serializer import TaskSerializer
from .filters import ToDoFilter
from rest_framework.pagination import PageNumberPagination
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
        filterset = ToDoFilter(request.GET, queryset= Task.objects.all().order_by('id')).qs
        if not filterset.exists():
            return Response({'message':'No Data'}, status=200)
        
        taskcount = filterset.count()

        paginator = PageNumberPagination()
        paginator.page_size = 2
        currnet_page = paginator.get_page_number(request,paginator)
        queryset = paginator.paginate_queryset(filterset,request)

        taskserializer = TaskSerializer(queryset, many=True)

        data = {
            "previous_page": paginator.get_previous_link(),
            "next_page": paginator.get_next_link(),
            "current_page": currnet_page,
            "total_pages" : paginator.page.paginator.num_pages,
            "tasks_Count": taskcount,
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