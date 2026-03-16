from tasks.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q


def save_new_task(task_form, user):
    # save a new task after submitn the form
    task = task_form.save(commit=False)
    task.user = user
    task.save()
    return task


def search_task(query, user):
    # search for the query on the database
    # tasks = Tasks.objects.filter(user=user).select_related('user').only(
    #                 'task', 'description', 'priority', 'date_added', 'user__username'
    #             )# Join the user table in ONE query instead of many

    
    tasks = Tasks.objects.filter(user=user).select_related('user').only(
        'task', 
        'status', 
        'priority', 
        'description', 
        'date_added',
        'user__username' # Only fetch the username, not the password hash!
    ).order_by('-priority', '-date_added')
    return tasks


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
