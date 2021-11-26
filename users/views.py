from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from TaskToDo import settings
from tasks.views import BoardsListView
from users.form import UserForm


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('all_tasks')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


class Register(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/register.html'
    success_url = '/'

    def get_success_url(self):
        # login
        self.object.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, self.object)
        # success url
        return ''


def logout_view(request):
    logout(request)
    return redirect('login')
