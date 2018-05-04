from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.


class HelloAPIView(APIView):
    serializer_class = serializers.HelloSerilizer

    def get(self, request, format=None):
        api_view = [
            'Hello',
            'Shafik',
            'Shaon'
        ]

        return Response({'message': 'Woooo!', 'api_view': api_view})

    def post(self, request):

        serializer = serializers.HelloSerilizer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
