from rest_framework import generics, permissions
from .models import CalorieEntry
from .serializers import CalorieEntrySerializer


class CalorieEntryList(generics.ListCreateAPIView):
    queryset = CalorieEntry.objects.all()
    serializer_class = CalorieEntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class CalorieEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CalorieEntry.objects.all()
    serializer_class = CalorieEntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]