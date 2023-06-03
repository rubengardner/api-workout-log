from django.db.models import Count
from rest_framework import generics, permissions, filters
from drf_workoutlog.permissions import IsOwnerOrReadOnly
from .models import Exercise
from .serializers import ExerciseSerializer

class ExerciseList(generics.ListCreateAPIView):
    """
    Return a list of all Exercises ordered by 
    created at
    """
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Exercise.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        queryset = super().get_queryset()
        
        if profile_id:
            queryset = queryset.filter(owner__id=profile_id)

        return queryset

class ExerciseSpecific(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve and update an Exercise only if the user is
    the owner of the Exercise
    """
    serializer_class = ExerciseSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Exercise.objects.all().order_by('-created_at')
