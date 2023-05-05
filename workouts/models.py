from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
   
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Workout n° {self.id} '