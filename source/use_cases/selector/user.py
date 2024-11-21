from source.models import CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login




class UserSelector:
    def list(self):
        return CustomUser.objects.all()
    
    def get_by_id(self,id):
        return get_object_or_404(CustomUser, pk= id)
    
        
    def login(self, username, password):
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(user)
