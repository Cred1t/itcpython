
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Todo


# Create your views here.
def home(request):
    title = 'Гланая страница'
    return render(request, 'home.html', {
        'title': title
    })


def about(request):
    title = 'Гланая страница'
    return render(request, 'about.html', {
        'title': title
    })


def time(request):
    time_now = datetime.now()
    return render(request, 'time.html', {
        'time_now': time_now
    })


def mywallet(request):
    wallet = 'Гланая страница'
    return render(request, 'mywallet.html', {
        'wallet': wallet
    })


def todo(request):
    todos_list = Todo.objects.all()

    return render(request, 'todo_list.html', {
        'todos': todos_list
    })


def todo_add(request):
    todo_name = request.GET.get('todo_name')
    new_todo = Todo(todo_name = todo_name)
    new_todo.save()

    return redirect('/todo')


def todo_delete(request):
    todo_id = request.GET.get('todo_id')
    todo = Todo.objects.get(id = todo_id)
    print('В базе наден: ', todo.todo_name)
    print('Мне ToDo ID келди: ', todo_id)

    delete = todo.delete()
    print('В базе данных удалено: ', delete)
    return redirect('/todo')