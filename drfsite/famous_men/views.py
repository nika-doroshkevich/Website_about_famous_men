from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FamousMen
from .serializers import FamousMenSerializer


class FamousMenAPIView(APIView):
    def get(self, request):
        w = FamousMen.objects.all()
        return Response({'posts': FamousMenSerializer(w, many=True).data})

    def post(self, request):
        serializer = FamousMenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = FamousMen.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )

        return Response({'post': FamousMenSerializer(post_new).data})
