from django.db import models
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    work_name = models.CharField(max_length=200)
    starting_date = models.DateField(default=timezone.now)
    ending_date = models.DateField(default=timezone.now)
    work_status = models.CharField(max_length=200)

    def __str__(self):
        return self.work_name
