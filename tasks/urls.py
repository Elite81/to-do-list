from django.urls import path
from .views  import *
urlpatterns = [
    path("", home, name = "home"),
    path("new_task/", add_task, name="new_task"),
    path("delete_task/", delete_task, name="delete_task"),
    path("edit/task", edit_task, name='edit_task'),
    path("search/", search, name="search")
]