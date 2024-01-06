from rest_framework import generics

from .models import FamousMen
from .serializers import FamousMenSerializer


class FamousMenAPIList(generics.ListCreateAPIView):
    queryset = FamousMen.objects.all()
    serializer_class = FamousMenSerializer


class FamousMenAPIUpdate(generics.UpdateAPIView):
    queryset = FamousMen.objects.all()
    serializer_class = FamousMenSerializer


class FamousMenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FamousMen.objects.all()
    serializer_class = FamousMenSerializer
