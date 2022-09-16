from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongsSerializer
from .models import Songs

# Create your views here.


@api_view(['GET', 'POST'])
def songs_list(request):
    songs = Songs.objects.all(request)
    serializer = SongsSerializer(songs, many = True)
    # if request.method == 'GET':

    return Response(serializer.data)
    






# @api_view(['GET', 'PUT', 'DELETE'])
