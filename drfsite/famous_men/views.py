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
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = FamousMen.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = FamousMenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance = FamousMen.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"error": "Object does not exist"})

        return Response({"post": "delete post " + str(pk)})
