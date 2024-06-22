# task/views.py

from django.shortcuts import render, get_object_or_404
from .models import Task, Category

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'tasks/category_list.html', {'categories': categories})
