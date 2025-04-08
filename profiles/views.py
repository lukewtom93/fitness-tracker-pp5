from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer
from api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]




