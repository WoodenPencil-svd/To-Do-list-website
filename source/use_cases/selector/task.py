from source.models import Task
from django.shortcuts import get_object_or_404
from source.use_cases.filters.task import TaskListFilter

class TaskSelector:
    def list(self,filters = None,*args, **kwargs) -> Task:
        filters = filters or {}
        query_set = Task.objects.all()
        return TaskListFilter(filters,query_set).qs


    def get_by_id(self, id: int, *args, **kwargs) -> Task:
        return get_object_or_404(Task, pk = id)
    
    def list_completed_by_id_user(self, id: int , *args, **kwargs) ->Task:
        task  = Task.objects.filter(user__id =id,status='completely').all()
        return task 
    
    def list_not_done_by_id_user(self, id: int, *args, **kwargs) -> Task:
        tasks = Task.objects.filter(user__id=id, status='not_done').all()
        return tasks

        
    
