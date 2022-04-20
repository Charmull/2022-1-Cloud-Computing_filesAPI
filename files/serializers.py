from rest_framework import serializers
from .models import File
from django.contrib.auth.models import User

class FileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # owner = serializers.StringRelatedField()

    class Meta:
        model = File
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    files = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='file-detail')

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'files']