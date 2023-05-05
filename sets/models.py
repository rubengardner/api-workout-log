from django.db import models
from exercises.models import Exercise
from workouts.models import Workout



class Set(models.Model):

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reps = models.PositiveIntegerField()
    value_of_unit_1 = models.IntegerField()
    value_of_unit_2 = models.IntegerField(default= None, blank=True)
   
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Set of: {self.exercise} '