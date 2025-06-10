from rest_framework import serializers
from .models import CalorieEntry


class CalorieEntrySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CalorieEntry
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        return CalorieEntry.objects.create(owner=user, **validated_data)