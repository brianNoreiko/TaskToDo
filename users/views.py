from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from TaskToDo import settings
from tasks.views import BoardsListView


class LoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task')


class Register(FormView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('login')
        return super(Register, self).get(*args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect('login')
