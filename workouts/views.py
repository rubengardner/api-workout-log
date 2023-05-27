from rest_framework.response import Response
from rest_framework import status, filters, generics
from rest_framework.views import APIView
from django.http import Http404
from .models import Workout
from django.db.models import Count
from .serializers import WorkoutSerializer
from drf_workoutlog.permissions import IsOwnerOrReadOnly


class WorkoutList(generics.ListCreateAPIView):
    """
    Return a list of all Workouts ordered by 
    created at
    """
    queryset = Workout.objects.annotate(
        sets_count=Count('set'),
        exercise_count=Count('set__exercise', distinct=True)
    ).order_by('-created_at')
    serializer_class = WorkoutSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WorkoutSpecific(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve and update a workout only if the user is
    the owner of the workout
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.annotate(
        sets_count=Count('set'),
        exercise_count=Count('set__exercise', distinct=True)
    ).order_by('-created_at')
