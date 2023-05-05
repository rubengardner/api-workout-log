from rest_framework.response import Response
from rest_framework import status, filters, generics
from rest_framework.views import APIView
from django.http import Http404
from .models import Set
from django.db.models import Count
from .serializers import SetSerializer
from drf_workoutlog.permissions import IsOwnerOrReadOnly


class SetList(generics.ListCreateAPIView):
    queryset = Set.objects.all( ).order_by('-created_at')
    serializer_class = SetSerializer



class SetSpecific(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SetSerializer
    queryset = Set.objects.all().order_by('-created_at')