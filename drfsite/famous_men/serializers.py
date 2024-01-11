from rest_framework import serializers
from .models import FamousMen


class FamousMenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FamousMen
        fields = "__all__"
