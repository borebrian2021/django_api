from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from .models import TestModel

from rest_framework.views import APIView

class simple(APIView):
    def post(self, request):
        new_test_content=TestModel.objects.create(
            name=request.data['name'],
            description =request.data['description'],
            phone_number = request.data['phone_number'],
            is_alive = request.data['is_alive'],
            amount = request.data['amount'],
        )
       
        return JsonResponse({"data":request.data})
        
       
    
    def get(self, request):
        content =TestModel.objects.all().values()
        return JsonResponse({"data":list(content)})