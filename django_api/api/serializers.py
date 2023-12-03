from rest_framework import serializers
from .models import PredictionValue

class PredictionValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionValue
        fields = '__all__'


class ImageEcgSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionValue
        fields = '__all__'