from rest_framework.response import Response
from rest_framework import status, filters, generics
from rest_framework.views import APIView
from django.http import Http404
from .models import Profile
from django.db.models import Count
from .serializers import ProfileSerializer
from drf_workoutlog.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all().order_by('-created_at')
    serializer_class = ProfileSerializer



class ProfileSpecific(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by('-created_at')