from django.shortcuts import render
from project import *

# Create your views here.

def home(request):
    if request.method == "POST":
        ...
    

    return render(request, "tasks/home.html")