from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MediaUpload, LogoUpload
from .serializers import MediaUploadSerializer, LogoUploadSerializer

class MediaUploadView(APIView):
    def post(self, request):
        serializer = MediaUploadSerializer(
            data=request.data,
            context={"request": request}  # ✅ add this
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MediaListView(APIView):
    def get(self, request):
        media = MediaUpload.objects.all()
        serializer = MediaUploadSerializer(
            media,
            many=True,
            context={"request": request}
        )
        return Response(serializer.data)
    
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny  # or IsAuthenticated if you want to protect
from .models import MediaUpload


class MediaDownloadView(APIView):
    permission_classes = [AllowAny]  # change to authenticated if needed
    

    def get(self, request, pk: int):
        media = get_object_or_404(MediaUpload, pk=pk)
        file_path = media.file.path          # full filesystem path
        filename = media.file.name.split('/')[-1]  # or media.file.name.rsplit('/', 1)[-1]

        # Optional: you can guess content type better, but octet-stream works for force-download
        response = FileResponse(
            open(file_path, 'rb'),
            as_attachment=True,
            filename=filename,
            # content_type='application/octet-stream'   # uncomment if you want to force octet-stream
        )
        return response
    
class LogoUploadView(APIView):
    def post(self, request):
        serializer = LogoUploadSerializer(
            data=request.data,
            context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoListView(APIView):
    def get(self, request):
        logos = LogoUpload.objects.all()
        serializer = LogoUploadSerializer(
            logos,
            many=True,
            context={"request": request}
        )
        return Response(serializer.data)
    
class LogoDownloadView(APIView):
    def get(self, request, pk: int):
        logo = get_object_or_404(LogoUpload, pk=pk)
        file_path = logo.file.path
        filename = logo.file.name.split('/')[-1]

        return FileResponse(
            open(file_path, 'rb'),
            as_attachment=True,
            filename=filename
        )