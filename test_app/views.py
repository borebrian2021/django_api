from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from .models import TestModel
from rest_framework import generics
from .serializers import SimpleSerializer
from rest_framework import generics



#GET $ PATCH
class SimpleGenerics(generics.ListCreateAPIView):
    queryset =TestModel.objects.all()
    serializer_class=SimpleSerializer
    
#PATCH OR PUT
class SimpleGenericsUpdate(generics.UpdateAPIView):
    queryset =TestModel.objects.all()
    serializer_class=SimpleSerializer
    lookup_field="id"
    
    