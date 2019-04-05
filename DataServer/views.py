from django.shortcuts import render
from django.http import Http404
from .models import *
from .serializers import *
from mongoengine import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework_mongoengine import generics

class GetJsonData(generics.ListCreateAPIView):
    queryset = GetData.objects.all()
    serializer_class = GetDataSerializer

class GetDatabyId(generics.RetrieveUpdateDestroyAPIView):
    queryset = GetData.objects.all()
    serializer_class = GetDataSerializer

class GetDatabyRating(generics.ListAPIView):
    queryset = GetData.objects.order_by('-Aggregate_rating')
    serializer_class = GetDataSerializer

class GetDatabyVotes(generics.ListAPIView):
    queryset = GetData.objects.order_by('-Votes')
    serializer_class = GetDataSerializer

class GetDatabyAvgCost(generics.ListAPIView):
    queryset = GetData.objects.order_by('-Average_Cost_for_two')
    serializer_class = GetDataSerializer

class GetFilterList(generics.ListAPIView):
    serializer_class = GetDataSerializer
    def get_queryset(self):
        queryset = GetData.objects.all()
        Cuisines = self.request.query_params.get('Cuisines', None)
        if Cuisines is not None:
            queryset = queryset.filter(Cuisines__contains=Cuisines)
        return queryset