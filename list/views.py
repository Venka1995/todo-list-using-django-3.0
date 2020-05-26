from django.shortcuts import render, redirect
from .models import Todo
from .forms import ListForm


# Create your views here.
def index(request):
    todo = Todo.objects.all()
    form = ListForm()
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {
        'todo': todo,
        'form': form
    }
    return render(request, 'list/index.html', context)


def update(request, pk):
    todo = Todo.objects.get(id=pk)
    form = ListForm(instance=todo)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'list/update.html', context)


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    context = {
        'todo': todo
    }
    return render(request, 'list/delete.html', context)
