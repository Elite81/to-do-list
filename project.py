from tasks.models import *
from django.shortcuts import get_object_or_404


def save_new_task(task_form, user):
    task = task_form.save(commit=False )
    task.user = user
    task.save()
    return task


def search_task(query):
    task = Tasks.objects.filter(Q(title__icontain=query) | Q(description__icontains=query))
    return task


def save_edited_task(form, user):
    task = form.save(commit=False)
    task.user = user
    task.save()
    return task

def delete_a_task(pk, user):
    task = get_object_or_404(Tasks, pk=pk, user=user)
    task.delete()
    return 
