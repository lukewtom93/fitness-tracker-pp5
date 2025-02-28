from rest_framework import serializers
from .models import Profile, Weight, CalorieEntry


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = '__all__'


class WeightSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Weight
        fields = '__all__'


class CalorieEntrySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CalorieEntry
        fields = '__all__'