from django.shortcuts import render

from rest_framework import generics

from music.models import Songs
from music.serializers import SongsSerializer

# Create your views here.
class ListSongsView(generics.ListAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
