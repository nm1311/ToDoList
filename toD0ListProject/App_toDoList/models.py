from django.db import models
from django.utils import timezone

class Todolist(models.Model):
    item_name = models.CharField(max_length = 100)
    is_complete = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)
    add_time = models.DateField(default=timezone.now)
    