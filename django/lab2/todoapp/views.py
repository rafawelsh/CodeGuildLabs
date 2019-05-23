from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo


def index(request):
    todos = Todo.objects.all().order_by('completed', 'created_date')#.order_by(created_date)
    return render(request, 'todoapp/index.html', {'todos':todos})

def toggle_todo(request, pk):
    todos = get_object_or_404(Todo, pk=pk)
    # todo = Todo.objects.get(pk=pk)
    todos.toggle_todo()
    return redirect('todoapp:index')

def add_todo(request):
    if request.method == 'POST':
        # print(request.POST)
        todo = request.POST['todo_text']
        todo = Todo(text=todo)
        todo.save()
    return redirect('todoapp:index')

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todoapp:index')

def edit_todo(request, pk):
    pass
