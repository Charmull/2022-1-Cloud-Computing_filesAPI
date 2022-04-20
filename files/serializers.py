from rest_framework import serializers
from .models import File
from django.contrib.auth.models import User

    # field_list = ['url', 'id', 'name', 'content', 'is_folder', 'expires_date', 'created_at', 'modified_at', 'owner', 'file', 'size', 'expires_date']

class FileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # owner = serializers.StringRelatedField()

    # def get_is_folder(self, obj):
    #     if obj.is_folder == False:
    #         global field_list
    #         field_list += ['file', 'size', 'expires_date']

    class Meta:
        model = File
        fields = ['url', 'id', 'name', 'content', 'is_folder', 'expires_date', 'created_at', 'modified_at', 'owner', 'file', 'size', 'expires_date']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    files = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='file-detail')

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'files']