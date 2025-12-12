import django_filters
from .models import Task

class ToDoFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(field_name='title', lookup_expr='contains')

    class Meta:
        model = Task
        fields = ['title', 'completed']