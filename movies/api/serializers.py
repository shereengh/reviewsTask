from rest_framework import serializers
from reviews.models import Review

class ReviewListSerializer(serializers.ModelSerializer):
    # Finish the serializer !