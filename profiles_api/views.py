from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


# Create your views here.

class HelloApiView(APIView):
    '''Test Api View'''

    def get(self, request, format=None):
        '''returns a list of APIView features'''
        an_apiview = [
            'uses HTTP functions such as (get, post, patch,put, delete)',
            'its similar to traditional django view',
            'gives youu the most control over your application',
            'its mapped manually to urls',
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})
