from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MediaUpload
from .serializers import MediaUploadSerializer

class MediaUploadView(APIView):
    def post(self, request):
        serializer = MediaUploadSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MediaListView(APIView):
    def get(self, request):
        media = MediaUpload.objects.all()
        serializer = MediaUploadSerializer(media, many=True)
        return Response(serializer.data)