from django.forms import ModelForm
from .models import *


class TaskForm(ModelForm):
    '''Task form '''
    class Meta:
        model = Tasks
        fields = [
            'task', 'status', 'priority', 'description'
        ]