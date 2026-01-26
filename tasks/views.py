from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from project import *
from .forms import *
from django.db.models import Q
from django.contrib import messages 

# Create your views here.

def home(request):
    tasks = Tasks.objects.select_related('user').all()
    return render(request, "tasks/home.html", {"tasks":tasks})



@login_required
def add_task(request):

    if request.method == "POST":
        task_from = TaskForm(request.POST)
        user = request.user
        if task_from.is_valid():
            task = save_new_task(task_from, user)
        messages.success(request, f'Your task:{task} is saved with success')
        return redirect("home")
    form = TaskForm()
    return render(request, "tasks/add_task.html", {"form": form})



@login_required
def delete_task(request, pk):
    user = user=request.user
    task_to_delete = get_object_or_404(Tasks, pk=pk, user=request.user)
    task = delete_a_task(pk,user)

    if request.user == task_to_delete.user:
        messages.success(request, f'Your task:{task} was deleted with success')
        return redirect("home")
    

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk, user=request.user)
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            user = request.user
            save_edited_task(form, user)
            messages.success(request, 'Your task was edited with success')
            return redirect("/")
    
    form = TaskForm(instance=task)
    return render(request, "tasks/edit_task.html", {"form": form, "task":task})


def search(request):
    query = request.GET.get('q').strip()
    if query:
        result = search_task(query)
        if not result.exists():
            messages.error(request, f"No Task found for the search {query}")
    else:
        
        messages.error('Your query is empty')
        return render(request, 'tasks/home.html')
    
    context = {'tasks':result, "query":query}
    return render(request, 'tasks/home.html', context)