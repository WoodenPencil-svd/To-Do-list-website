
from source.models import Task 
from django.db import transaction
from dataclasses import dataclass

@dataclass
class TaskService:
    @transaction.atomic
    def create(self, input:dict, *args, **kwargs):
        task = Task.objects.create(**input)
        return task
    
    @transaction.atomic
    def update(self,id , *args, **kwargs):
       task = Task.objects.filter(pk =id).update(**kwargs)
       return task
   
    @transaction.atomic
    def delete(self,id,*args, **kwargs):
        Task.objects.get(pk=id).delete()
        
    @transaction.atomic
    def mark_done(self,id,*args, **kwargs):
        task = Task.objects.get(pk = id)
        task.status = 'completely'
        task.save()
        return task
