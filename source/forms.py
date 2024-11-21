# forms.py
from django.contrib.auth.forms import UserCreationForm
from source.models import CustomUser

class UserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','is_active','is_superuser']


