from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )

class Tasks(models.Model):
    
    STATUS_CHOISES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("compted", "Completed")
    ]
    PRIORITY = [
        ("low","Low"),
        ("medium","Medium"),
        ("high","High")
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    user= models.ForeignKey("User", on_delete=models.CASCADE, related_name="tasks", unique=True)
    task= models.CharField(max_length=256, blank=False, null=False)
    status =  models.CharField(max_length=64, choices= STATUS_CHOISES, default=STATUS_CHOISES[1][0] )
    priority = models.CharField(max_length=64, choices= PRIORITY, default=PRIORITY[0][0] )
    description = models.TextField(blank=True)
    date_added= models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)