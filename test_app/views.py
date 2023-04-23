from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from .models import TestModel
from rest_framework import generics
from .serializers import SimpleSerializer
from rest_framework import generics



    
class SimpleGenerics(generics.ListCreateAPIView):
    queryset =TestModel.objects.all()
    serializer_class=SimpleSerializer
    