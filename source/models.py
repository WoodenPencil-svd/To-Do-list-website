from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType



class UserManager(BaseUserManager):
    def create_user(self, username, password = None):
        user = self.model(username=username)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,username , password = None):
        user = self.create_user(username,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using =self._db)
  

class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    
    USERNAME_FIELD = 'username'  
    REQUIRED_FIELDS  = []
    def __str__(self):
        return self.username
    
    def set_permission(self,user):
        if not self.is_staff or not self.is_superuser:
            content_type = ContentType.objects.get_for_model(CustomUser)  
            permission, created = Permission.objects.get_or_create(
            codename='only_view_dashboard',
            name='Only View Dashboard',
            content_type=content_type
            )
            self.user_permissions.set([permission])
    
class Task(models.Model):
    
    STATUS_CHOICES = [ 
        ('not_done','Not Done'),
        ('completely','Completely'),
    ]
    
    title = models.CharField(_("Title"), max_length=255,null=False)
    user = models.ForeignKey(CustomUser, verbose_name=_("User"), on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='not_done',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    
    
        
 
 


