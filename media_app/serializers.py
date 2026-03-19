from rest_framework import serializers
from .models import MediaUpload

class MediaUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaUpload
        fields = '__all__'
        