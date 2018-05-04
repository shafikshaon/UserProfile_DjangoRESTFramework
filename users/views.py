from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class HelloAPIView(APIView):
    def get(self, request, format=None):
        api_view = [
            'Hello',
            'Shafik',
            'Shaon'
        ]

        return Response({'message': 'Woooo!', 'api_view': api_view})