from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import FamousMen
from .serializers import FamousMenSerializer


class FamousMenViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    queryset = FamousMen.objects.all()
    serializer_class = FamousMenSerializer
