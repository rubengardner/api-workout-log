from django.db import models
from django.contrib.auth.models import User
import datetime

class Workout(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=datetime.date.today)
   
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Workout n° {self.id} '