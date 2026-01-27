from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("new_task/", add_task, name="new_task"),
    path("delete/task/<uuid:pk>", delete_task, name="delete_task"),
    path("edit_task/<uuid:pk>", edit_task, name="edit_task"),
    path("search/", search, name="search"),
    path("view_task/<uuid:pk>", view_taks, name="view_task"),
]
