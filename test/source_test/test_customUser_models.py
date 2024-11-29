import pytest

from source.use_cases.selector.user import UserSelector
from source.use_cases.service.user import UserService
from source.use_cases.filters.user import UserListFilter
from source.models import *


@pytest.mark.django_db
class TestUser: 
    def test_user_create(self,):
        input_data  = { 
            "username":"Test",
            "password":"Test123",
            "is_active":True,
            "is_superuser":False
        }
        user = UserService.create(self,input=input_data)
        assert user.id is not None
        assert user.username == input_data.get('username')
        
    def test_user_get_by_id(self,):
        input_data  = { 
            "username":"Test",
            "password":"Test123",
            "is_active":True,
            "is_superuser":False
        }
        user = UserService.create(self,input=input_data)
        output = UserSelector.get_by_id(self,id=user.id)
        assert output.username == user.username
        
    def test_user_get_list(self,):
        input_data  = { 
            "username":"Test",
            "password":"Test123",
            "is_active":True,
            "is_superuser":False
        }
        user = UserService.create(self,input=input_data)
        output = UserSelector.list(self)
        assert output.count() == 1 
        
    def test_user_get_list_with_filter(self,):
        input_data  = { 
            "username":"Test",
            "password":"Test123",
            "is_active":True,
            "is_superuser":False
        }
        filter = {
            "username":"Test"
        }
        user = UserService.create(self,input=input_data)
        user_list = UserSelector.list(self)
        ouput = (UserListFilter(filter,user_list).qs).values()
        assert ouput.first().get('username') == input_data.get('username')
    
    def test_user_delete_by_id(self,):
        input_data  = { 
            "username":"Test",
            "password":"Test123",
            "is_active":True,
            "is_superuser":False
        }
        user = UserService.create(self,input=input_data)
        UserService.delete(self,id=user.id)
        output = UserSelector.list(self)
        assert output.count()== 0 
    