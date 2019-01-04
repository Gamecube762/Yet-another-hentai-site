from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, QueryDict
from hentai.models import *
from hentai.serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from itertools import chain

# Create your views here.


# The general view
class SeriesSerializerView(APIView):
    def get(self, request, format=None):
        try:
            queryset = Series.objects.all().order_by('series_name')
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SeriesSerializer(queryset, many=True)
        return Response(serializer.data)

# Displays all the info about a series
class IdSeriesDetailSerializerView(APIView):
    def get(self, request, pk, format=None):
        try:
            queryset = Series.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SeriesDetailSerializer(queryset)
        return Response(serializer.data)

class NameSeriesDetailSerializerView(APIView):
    def get(self, request, name, format=None):
        try:
            queryset = Series.objects.get(series_name=name.title())
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SeriesDetailSerializer(queryset)
        return Response(serializer.data)

# Displays the info about the video with all of the info about the tags
class VideoDetailSerializerView(APIView):
    def get(self, request, pk, format=None):
        try:
            queryset = Video.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = VideoDetailSerializer(queryset)
        return Response(serializer.data)

class VideoSeriesSerializerView(APIView):
    def get(self, request, name, pk, format=None):
        try:
            queryset = Series.objects.get(series_name=name.title()).videos.get(episode=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = VideoDetailSerializer(queryset)
        return Response(serializer.data)

# Shows videos with any of the given tags
class AnyTagsSerializerView(APIView):
    def get(self, request, tags, format=None):
        if '.' in tags:
            tag_list = list(tags.split('.'))
        else:
            tag_list = list(tags)

        try:
            queryset = []
            for tag in tag_list:
                to_merge = VideoTag.objects.get(pk = int(tag)).tags.all().order_by('series__series_name')
                queryset = list(chain(queryset, to_merge))
            
            queryset = set(queryset)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)

# Shows videos with all of the given tags
class AllTagsSerializerView(APIView):
    def get(self, request, tags, format=None):
        if '.' in tags:
            tag_list = list(tags.split('.'))
        else:
            tag_list = list(tags)

        try:
            queryset = []
            for tag in tag_list:
                to_merge = VideoTag.objects.get(pk = int(tag)).tags.all().order_by('series__series_name')
                if (len(queryset) == 0):
                    queryset = VideoTag.objects.get(pk = int(tag)).tags.all().order_by('series__series_name')
                else:
                    queryset = list(set(queryset).intersection(to_merge))
            
            queryset = set(queryset)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)