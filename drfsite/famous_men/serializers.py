from rest_framework import serializers
from .models import FamousMen


class FamousMenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamousMen
        fields = "__all__"
