from example.models import Example
from rest_framework import serializers

class ExampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Example
        fields = ['field1','field2','field3','field4','field5','created']
