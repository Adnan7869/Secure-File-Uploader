from rest_framework import serializers
from .models import UploadedFile

class UploadFileSerializer(serializers.ModelSerializer):
    class meta:
        model = UploadedFile
        fields = '__all__'
        