from django.shortcuts import render
from rest_framework import generics

# Create your views here.
class Index(generics.ListAPIView):
    def get(self, request):
        pass