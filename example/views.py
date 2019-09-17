from django.shortcuts import render
from rest_framework import viewsets

from example.models import Example
from example.serializers import ExampleSerializer


class ExampleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Examples to be viewed or edited.
    """
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
