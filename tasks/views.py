# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

import tasks
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


def all_tasks(request):
    tasks = Task.objects.all()
    return render(request,
                  'tasks/taskView.html',
                  {tasks: tasks}
                  )


class deleteTask(LoginRequiredMixin, DeleteView):
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

def jsonBoards(request, id):
    data = serialize("json", Board.objects.filter(owner_id=id))
    return JsonResponse(data, status=200, safe=False)

class CreateBoard(CreateView):
    template_name = 'tasks/boardForm.html'
    model = Board
    fields = ['name']
    success_url = 'boards'
