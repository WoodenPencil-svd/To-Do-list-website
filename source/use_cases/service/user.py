from source.models import CustomUser as UserModel
from source.entities.user import User as UserEntity
from django.db import transaction


class UserService:
    @transaction.atomic
    def create(self, entity:UserEntity,*args, **kwargs):
        user = UserModel.objects.create(self,**entity)
        return user
    
    @transaction.atomic
    def delete(self,id,*args, **kwargs):
        UserModel.objects.get(pk = id ).delete()
    
    @transaction.atomic
    def update(self, id , *args, **kwargs):
        UserModel.objects.filter(pk = id).update(**kwargs)
        
        
    