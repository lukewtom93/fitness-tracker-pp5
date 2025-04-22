from rest_framework import generics, permissions
from .models import CalorieEntry
from .serializers import CalorieEntrySerializer


class CalorieEntryList(generics.ListCreateAPIView):
    queryset = CalorieEntry.objects.all()
    serializer_class = CalorieEntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CalorieEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CalorieEntry.objects.all()
    serializer_class = CalorieEntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]