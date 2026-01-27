from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from project import *
from .forms import *
from django.db.models import Q
from django.contrib import messages

# Create your views here.


def home(request):
    tasks = Tasks.objects.select_related("user").all().order_by("-priority", "-date_added")
    return render(request, "tasks/home.html", {"tasks": tasks})


@login_required
def add_task(request):

    if request.method == "POST":
        task_from = TaskForm(request.POST)  # Getting the form with the data submitted
        user = request.user
        if task_from.is_valid():  # validating the form
            task = save_new_task(task_from, user)  # Helper function
        messages.success(request, f"Your task:{task} is saved with success")
        return redirect("home")
    form = TaskForm()
    return render(request, "tasks/add_task.html", {"form": form})


@login_required
def delete_task(request, pk):
    user = user = request.user
    task_to_delete = get_object_or_404(
        Tasks, pk=pk, user=request.user
    )  # getting the task from the database
    task = delete_a_task(pk, user)

    if (
        request.user == task_to_delete.user
    ):  # insure the the user is the owner of the the task
        messages.success(request, f"Your task:{task} was deleted with success")
        return redirect("home")
    else:
        messages.success(request, f"You are not the auther of the task:{task}")
        return redirect("home")


@login_required
def edit_task(request, pk):
    task = get_object_or_404(
        Tasks, pk=pk, user=request.user
    )  # Query the database to get the task to edit

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():  # validating the form
            user = request.user
            save_edited_task(form, user)
            messages.success(request, "Your task was edited with success")
            return redirect("/")

    form = TaskForm(instance=task)
    return render(request, "tasks/edit_task.html", {"form": form, "task": task})


def search(request):
    query = request.GET.get("q").strip()  # getting the query
    if query:
        result = search_task(query)
        if not result.exists():  # if search does not return a result
            messages.error(request, f"No Task found for the search {query}")
    else:
        messages.error("Your query is empty")
        return render(request, "tasks/home.html")

    context = {"tasks": result, "query": query}
    return render(request, "tasks/home.html", context)
