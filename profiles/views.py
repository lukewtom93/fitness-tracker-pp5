from rest_framework import generics, permissions
from .models import Profile, Weight, CalorieEntry
from .serializers import ProfileSerializer, WeightSerializer, CalorieEntrySerializer


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WeightList(generics.ListCreateAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CalorieEntryList(generics.ListCreateAPIView):
    queryset = CalorieEntry.objects.all()
    serializer_class = CalorieEntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]