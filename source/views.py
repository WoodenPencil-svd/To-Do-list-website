from django.views import View
from django.views.generic import FormView,TemplateView,RedirectView
from django.urls import reverse_lazy as _
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from source.models import *
from source.forms import *

from source.use_cases.selector.task import TaskSelector 
from source.use_cases.service.task import TaskService


class IndexView(TemplateView):
    template_name = 'index.html'

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        tasks_completed = TaskSelector.list_completed_by_id_user(self, id=request.user.id)
        tasks_not_done = TaskSelector.list_not_done_by_id_user(self, id=request.user.id)
        context = {
            'tasks_not_done': tasks_not_done,
            'task_completed': tasks_completed
        }
        return render(request, self.template_name, context)
class AddPostView(View):
    def post(self, request):
        task_title = request.POST.get('task')
        if task_title:  # Add new task
            data_input = {
                'title': request.POST.get('task'),
                'user_id': request.user.id
            }
            TaskService.create(self, input=data_input)
        return redirect('home')

class MarkAsDoneView(View):
    def post(self,request,task_id):
        TaskService.mark_done(self, id=task_id)
        return redirect('home')
    
class DeleteTaskView(View):
    def post(self, request, task_id):
        TaskService.delete(self, id=task_id)
        return redirect('home')

class LoginView(FormView):
    template_name = 'login.html'
    success_url = _('home')
    form_class = AuthenticationForm
    fail_url = _('login')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect(self.get_success_url())
        else: 
            return self.form_invalid(form)
    
class SignupView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = _('login')

    def form_valid(self, form):
        form.save()
        return redirect(self.get_success_url())
    
class LogoutView(RedirectView):
    success_url = _('index')
    def get(self, request):
        logout(request)
        return redirect(self.success_url)
    
     

        

