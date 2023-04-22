from rest_framework import serializers
from .models import TestModel

class SimpleSerializer(serializers.Serializer):

    class Meta:
        model = TestModel
        # fields=("name","description",)
        fields="__all__"