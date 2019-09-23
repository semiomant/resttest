from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # requirement: do it the official way =/
    # def _check_token(self,data_dict):
    #     """check in more detail in advanced version"""
    #     return 'sam-token' in data_dict

    def list(self, request):
        queryset = Example.objects.all()
        seri = ExampleSerializer(queryset, many=True)
        return Response(seri.data)

    @action(detail=False, methods=['get','post'])
    def testaction(self, request):
        get_data = request.GET.dict()
        post_data = request.POST.dict()
        # if self._check_token(get_data):
            # return Response({'get':str(get_data), 'post': str(post_data)})
        # else:
        #     return Response({'i_know_now': 'you should not be here!'},
        #     status=status.HTTP_417_EXPECTATION_FAILED)
        return Response({'get':str(get_data), 'post': str(post_data)})
