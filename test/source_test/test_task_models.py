import pytest

from source.use_cases.selector.task import TaskSelector
from source.use_cases.service.task import TaskService
from source.use_cases.filters.task import TaskListFilter
from source.models import *

@pytest.mark.django_db
class TestTask: 
    def test_task_create(self):
        # Tạo user
        user = CustomUser.objects.create(username='admin')
        # Input
        input_data = {
            "title": "code",
            "user": user,
            "status": "not_done"
        }
        # Action
        output = TaskService.create(self,input=input_data)
        # Assert
        assert output.id is not None, "Task ID should not be None"
        assert output.title == input_data["title"], "Task title mismatch"
        
    def test_task_get_by_id(self,):
        user = CustomUser.objects.create(username='admin')
        # Input
        input_data = {
            "title": "code",
            "user": user,
            "status": "not_done"
        }
        task = TaskService.create(self,input=input_data)
        #action
        output = TaskSelector.get_by_id(self,id= task.id)
        # assert
        assert output.title == task.title
        assert output.status == task.status
        
    def test_task_get_list(self,):
        # Input
        user = CustomUser.objects.create(username='admin')
        input_data = {
            "title": "code",
            "user": user,
            "status": "not_done"
        }
        task = TaskService.create(self,input=input_data)
        #action
        output = TaskSelector.list(self)
        #assert
        assert output.count() == 1
        
    def test_task_get_list_with_filter(self,):
        # Input
        user = CustomUser.objects.create(username='admin')
        input_data = {
            "title": "code",
            "user": user,
            "status": "not_done"
        }
        filter = {
            "title": "code",
        }

        task = TaskService.create(self,input=input_data)
        #action
        query_set= Task.objects.all()
        output = (TaskListFilter(filter, query_set).qs).values()
        # assert
        assert  output.first().get("title") == task.title

    def test_task_delete_by_id(self,):
        user = CustomUser.objects.create(username='admin')
        input_data = {
            "title": "code",
            "user": user,
            "status": "not_done"
        }
        filter = {
            "name": "Test ModuleFactor",
        }
        task = TaskService.create(self,input=input_data)
        TaskService.delete(self, id=task.id)
        output = TaskSelector.list(self)
        assert output.count() == 0
        
        
    
    

