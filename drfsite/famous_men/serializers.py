from rest_framework import serializers

from .models import FamousMen, Category


class FamousMenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FamousMen
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    people_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'people_count']
