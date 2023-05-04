from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    unit_choices = [
        ('kg', 'kg'), ('sec', 'sec'),
        ('m', 'm')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True)
    
    unit_1 = models.CharField(max_length=40, choices=unit_choices, default='kg')
    unit_2 = models.CharField(max_length=40, choices=unit_choices, default= None)
   
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name}'