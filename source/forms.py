# forms.py
from django.contrib.auth.forms import UserCreationForm
from source.models import CustomUser
from django import forms
class UserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username',]

class TaskForm(forms.Form):
    task = forms.CharField(max_length=255, required=True)

