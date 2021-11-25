from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default="Board")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='boards')

    def __str__(self):
        return self.name

    @staticmethod
    def is_owner(self, user):
        is_owner = False

        if user.id == self.owner.id:
            is_owner = True

        return is_owner


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default="Category")
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='categories')

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        inProgress = 'En proceso'
        finished = 'Finalizado'
        toDo = 'Pendiente'

    user = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.toDo)

    def __str__(self):
        return self.title
