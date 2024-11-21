from django.shortcuts import render
from source.use_cases.selector.user import UserSelector
from source.use_cases.service.user import UserService
from django.views.generic import FormView,TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from source.forms import UserCreationForm

class HomeView(TemplateView):
    template_name = 'home.html'
    
class LoginView(FormView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            try:
                UserSelector.login(self.request, form.cleaned_data['username'], form.cleaned_data['password'])
                return redirect(self.get_success_url())
            except ObjectDoesNotExist:
                form.add_error(None, "User does not exist")
        return self.form_invalid(form)
    
class SignupView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        entity = form.cleaned_data
        user = UserService.create(entity)
        return redirect(self.get_success_url())