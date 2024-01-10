from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import FamousMen, Category
from .serializers import FamousMenSerializer


class FamousMenViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    queryset = FamousMen.objects.all()
    serializer_class = FamousMenSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return FamousMen.objects.all()[:3]

        return FamousMen.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        categories = Category.objects.get(pk=pk)
        return Response({'categories': categories.name})
