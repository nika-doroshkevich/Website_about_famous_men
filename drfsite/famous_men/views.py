from rest_framework import generics
from .models import FamousMen
from .serializers import FamousMenSerializer


class FamousMenAPIView(generics.ListAPIView):
    queryset = FamousMen.objects.all()
    serializer_class = FamousMenSerializer
