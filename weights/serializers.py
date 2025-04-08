from rest_framework import serializers
from .models import Weight
from profiles.models import Profile


class WeightSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())

    class Meta:
        model = Weight
        fields = '__all__'