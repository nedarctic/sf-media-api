from rest_framework import serializers
from .models import MediaUpload, LogoUpload

class MediaUploadSerializer(serializers.ModelSerializer):
    download_url = serializers.SerializerMethodField()

    class Meta:
        model = MediaUpload
        fields = ['id', 'file', 'uploaded_at', 'download_url']

    def get_download_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f"/api/files/{obj.id}/download/")
    
class LogoUploadSerializer(serializers.ModelSerializer):
    download_url = serializers.SerializerMethodField()

    class Meta:
        model = LogoUpload
        fields = ['id', 'file', 'uploaded_at', 'download_url']

    def get_download_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f"/api/files/{obj.id}/download/")