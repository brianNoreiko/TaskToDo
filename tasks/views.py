# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from tasks.models import Task, Board


class createTask(CreateView):
    model = Task
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('all_tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(createTask, self).form_valid(form)


class updateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('all_tasks')


class detailTask(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task.html'


"""def all_tasks(request):
    tasks = Task.objects.all()
    return render(request,
                  'tasks/task_list.html',
                  {tasks: tasks}
                  )
"""


class TasksListView(ListView, LoginRequiredMixin):
    model = Task
    context_object_name = 'listTasks'

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listTasks'] = context['listTasks'].filter(user=self.request.user)
        return context


class deleteTask(LoginRequiredMixin, DeleteView):
    template_name = 'tasks/task_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('all_tasks')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


class BoardsListView(ListView):
    model = Board
    context_object_name = 'listBoards'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listBoards'] = context['listBoards'].filter(owner=self.request.user)
        return context


class CreateBoard(CreateView):
    template_name = 'tasks/boardForm.html'
    model = Board
    fields = ['name']
    success_url = 'boards'
