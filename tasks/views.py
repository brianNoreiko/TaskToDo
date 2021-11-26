# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from tasks.models import Task, Board


class createTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):  # asigna el usuario que crea la Task, al objeto task
        form.instance.user = self.request.user
        return super(createTask, self).form_valid(form)


class updateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('tasks')


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
    success_url = reverse_lazy('tasks')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


class BoardsListView(ListView,LoginRequiredMixin):
    model = Board
    context_object_name = 'boards'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boards'] = context['boards'].filter(user=self.request.user)
        return context


    def jsonTasks(request, id):
        data = serialize("json", Task.objects.filter(user=id))
        return JsonResponse(data, status=200, safe=False)

    #template_name = 'tasks/boardList.html'
    #def get_queryset(self):
    #    self.user = get_object_or_404(User, name=self.kwargs[''])
    #    return Board.objects.filter(user=self.user)


class CreateBoard(CreateView):
    template_name = 'tasks/boardForm.html'
    model = Board
    fields = ['name']
    success_url = 'boardList.html'
