from django.shortcuts import render

from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_mongoengine import generics

class getDataList(generics.ListCreateAPIView):
    queryset = GetData.objects.all()
    serializer_class = GetDataSerializer

class getData_expt_get(generics.RetrieveUpdateDestroyAPIView):
    queryset = GetData.objects.all()
    serializer_class = GetDataSerializer
