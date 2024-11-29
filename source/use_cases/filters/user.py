import django_filters
from source.models import CustomUser

class UserListFilter(django_filters.FilterSet):    
    class Meta:
        model = CustomUser
        fields = {
            'username': ['icontains'],
            
        }
