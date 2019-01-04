from rest_framework import serializers
from hentai.models import *

# Classes needed to use the API

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoTag
        fields = ('id', 'tag_name')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'episode', 'upload_date', 'file_path', 'tags')

class VideoDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many = True, read_only = True)

    class Meta:
        model = Video
        fields = ('id', 'episode', 'upload_date', 'file_path', 'tags')

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name')

class DescriptionSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only = True)

    class Meta:
        model = Description
        fields = ('title', 'description', 'language')

class SeriesDetailSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many = True, read_only = True)
    description = DescriptionSerializer(many = True, read_only = True)

    class Meta:
        model = Series
        fields = ('id', 'series_name', 'description', 'videos')

class SeriesSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many = True, read_only = True)

    class Meta:
        model = Series
        fields = ('id', 'series_name', 'videos')