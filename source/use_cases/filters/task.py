import django_filters
from source.models import Task

class TaskListFilter(django_filters.FilterSet):    
    class Meta:
        model = Task
        fields = {
            'title': ['icontains'],
            
        }
