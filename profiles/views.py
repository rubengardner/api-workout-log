from rest_framework.response import Response
from rest_framework import status, filters, generics
from rest_framework.views import APIView
from django.http import Http404
from .models import Profile
from django.db.models import Count
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all().order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
    ]
    ordering_fields = [
    ]


class ProfileSpecific(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by('-created_at')