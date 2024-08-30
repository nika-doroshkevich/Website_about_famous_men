from django.db.models import Count
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import FamousMen, Category
from .permissions import IsAdminOrReadOnly
from .serializers import FamousMenSerializer, CategorySerializer


class WomenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class FamousMenAPIList(generics.ListCreateAPIView):
    queryset = FamousMen.objects.select_related('category', 'user').all()
    serializer_class = FamousMenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenAPIListPagination


class FamousMenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = FamousMen.objects.select_for_update().all()
    serializer_class = FamousMenSerializer
    permission_classes = (IsAuthenticated,)


class FamousMenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = FamousMen.objects.all()
    serializer_class = FamousMenSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CategoryPeopleCountView(generics.GenericAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.annotate(people_count=Count('famousmen')).values('name', 'people_count')
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class FamousMenCountView(generics.GenericAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        count = FamousMen.objects.aggregate(total_count=Count('id'))
        return Response(count)
