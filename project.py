from tasks.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q


def save_new_task(task_form, user):
    # save a new task after submitn the form
    task = task_form.save(commit=False)
    task.user = user
    task.save()
    return task


def search_task(query):
    # search for the query on the database
    task = Tasks.objects.filter(
        Q(task__icontains=query) | Q(description__icontains=query)
    )
    return task


def save_edited_task(form):
    # save the edited task
    task = form.save(commit=False)
    task.save()
    return task


def delete_a_task(pk, user):
    # Deleted the edited task
    task = get_object_or_404(Tasks, pk=pk, user=user)
    task.delete()
    return
