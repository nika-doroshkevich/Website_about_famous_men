from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import FamousMen
from .permissions import IsAdminOrReadOnly
from .serializers import FamousMenSerializer


class WomenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class FamousMenAPIList(generics.ListCreateAPIView):
    queryset = FamousMen.objects.all()
    serializer_class = FamousMenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenAPIListPagination


class FamousMenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = FamousMen.objects.all()
    serializer_class = FamousMenSerializer
    permission_classes = (IsAuthenticated,)


class FamousMenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = FamousMen.objects.all()
    serializer_class = FamousMenSerializer
    permission_classes = (IsAdminOrReadOnly,)
