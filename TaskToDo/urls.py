"""TaskToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import users.views
from django.contrib import admin
from django.urls import path
from tasks.views import CreateBoard, BoardsListView, createTask, updateTask, deleteTask, detailTask, \
    TasksListView
from users.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    ##path('tasks/boardForm/', CreateBoard.as_view()),'newBoard',
    ##path('tasks/boardList', BoardsListView.as_view()), name='boardList',
    path('', users.views.loginView, name='login'),
    path('logout/', users.views.logout_view, name='logout'),
    path('tasks/', TasksListView.as_view(), name='all_tasks'),
    path('register/', users.views.Register.as_view(), name='register'),
    ##path('task/<int:pk>/', detailTask.as_view(), name='task'),
    path('task-create/', createTask.as_view(), name='createTask'),
    path('task-update/<int:pk>/', updateTask.as_view(), name='updateTask'),
    path('task-delete/<int:pk>/', deleteTask.as_view(), name='deleteTask'),
]
