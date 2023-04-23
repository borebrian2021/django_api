from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from .models import TestModel
from .serializers import SimpleSerializer
from rest_framework import viewsets


#GET $ PATCH
class SimpleViewset(viewsets.ModelViewSet):
    queryset =TestModel.objects.all()
    serializer_class=SimpleSerializer
    