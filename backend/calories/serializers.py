from rest_framework import serializers
from .models import CalorieEntry


class CalorieEntrySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CalorieEntry
        fields = '__all__'