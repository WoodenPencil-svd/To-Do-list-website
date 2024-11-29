from source.models import CustomUser as UserModel
from django.contrib.auth.hashers import make_password
from django.db import transaction

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class UserService:
    @transaction.atomic
    def create( self,input:dict  ,*args, **kwargs):
        input['password'] = make_password(input['password']) #hash password
        user = UserModel.objects.create(**input)
        return user
    
    @transaction.atomic
    def delete(self,id,*args, **kwargs):
        UserModel.objects.get(pk = id ).delete()
    
    @transaction.atomic
    def update(self, id , *args, **kwargs):
        UserModel.objects.filter(pk = id).update(**kwargs)
        
    @transaction.atomic
    def login(self,username,password,*args, **kwargs):
        user = authenticate(username=username, password =password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            all_permissions = list(user.get_all_permissions())
            return {   
                'token': token.key,
                'user id': user.pk,
                'username': user.username,
                'is_authenticated': user.is_authenticated,
                'permissions': all_permissions or [],
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser
                }
       


        
        
        
    