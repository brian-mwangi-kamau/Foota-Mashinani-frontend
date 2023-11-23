# serializers.py
from rest_framework import serializers

class ClubSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    # Add other fields as needed
