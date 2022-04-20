from rest_framework import serializers
from .models import File

class FileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = File
        fields = '__all__'