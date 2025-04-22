from rest_framework import serializers
from .models import Ad


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["image", "link", "title", "description"]
