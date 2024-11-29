from source.models import CustomUser
from django.shortcuts import get_object_or_404
from source.use_cases.filters.user import UserListFilter





class UserSelector:
    def list(self,filters = None)-> CustomUser:
        filters = filters or {}
        query_set = CustomUser.objects.all()
        return UserListFilter(filters,query_set).qs
    
    def get_by_id(self,id) ->CustomUser:
        return get_object_or_404(CustomUser, pk= id)
    
        
         