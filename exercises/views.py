from django.db.models import Count
from rest_framework import generics, permissions, filters
from drf_workoutlog.permissions import IsOwnerOrReadOnly
from .models import Exercise
from .serializers import ExerciseSerializer

class ExerciseList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Exercise.objects.all().order_by('-created_at')


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class ExerciseSpecific(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ExerciseSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Exercise.objects.all().order_by('-created_at')