from rest_framework import serializers
from .models import FamousMen


class FamousMenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamousMen
        fields = ('title', 'category_id')
