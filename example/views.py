from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

from example.models import Example
from example.serializers import ExampleSerializer


class ExampleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Examples to be viewed or edited.
    """
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer

class Example2ViewSet(viewsets.ModelViewSet):
    """
    experiment with overriding stuff to customize
    """
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer

    def list(self, request):
        # queryset = Example.objects.all()
        # seri = ExampleSerializer(queryset, many=True)
        # return Response(seri.data)
        return HttpResponse(str(request.GET.dict()))
