from rest_framework.response import Response
from rest_framework import status, filters, generics, permissions
from rest_framework.views import APIView
from django.http import Http404
from .models import Set
from django.db.models import Count
from .serializers import SetSerializer
from drf_workoutlog.permissions import IsOwnerOrReadOnly


class SetList(generics.ListCreateAPIView):
    """
    Return a list of all sets ordered by 
    created at
    """
    queryset = Set.objects.all().order_by('-created_at')
    serializer_class = SetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SetSpecific(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve and update a set only if the user is
    the owner of the set
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SetSerializer
    queryset = Set.objects.all().order_by('-created_at')
