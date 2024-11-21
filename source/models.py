from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _



class UserManager(BaseUserManager):
    def create_user(self, username, password = None):
        user = self.model(username=username)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_super_user(self,username , password):
        user = self.create_user(username,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using =self._db)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255,unique=True)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    objects = UserManager()    
    USERNAME_FIELD = 'username'  
    REQUIRED_FIELDS  = []
    def __str__(self):
        return self.username
    
class Task(models.Model):
    
    STATUS_CHOICES = [ 
        ('not_done','Not Done'),
        ('completely','Completely'),
    ]
    
    title = models.CharField(_("Name"), max_length=255)
    description = models.CharField(_("Description"), max_length=255)
    user = models.ForeignKey(CustomUser, verbose_name=_("User"), on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='not_done',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
        
 
 


