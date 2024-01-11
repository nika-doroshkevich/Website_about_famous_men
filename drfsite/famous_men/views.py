from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import FamousMen
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .serializers import FamousMenSerializer


class FamousMenAPIList(generics.ListCreateAPIView):
    queryset = FamousMen.objects.all()
    serializer_class = FamousMenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FamousMenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = FamousMen.objects.all()
    serializer_class = FamousMenSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class FamousMenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = FamousMen.objects.all()
    serializer_class = FamousMenSerializer
    permission_classes = (IsAdminOrReadOnly,)
