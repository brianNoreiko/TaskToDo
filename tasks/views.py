from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404
from tasks.models import *



class BoardsListView(ListView):
    template_name = 'tasks/boardList.html'
    def get_queryset(self):
        self.user = get_object_or_404(User, name =self.kwargs['usuario'])
        return Board.objects.filter(user=self.user)

class CreateBoard(CreateView):
    template_name = 'tasks/boardForm.html'
    model = Board
    fields = ['name']
    success_url = ''