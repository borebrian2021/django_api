from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from .models import TestModel
from rest_framework.views import APIView
from .serializers import SimpleSerializer
class Simple(APIView):
    def post(self, request):
        
        # VALIDATING THE DATA INPUT
        serializer= SimpleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # CREATING AND INSERTING THE NEW DATA
        new_test_content=TestModel.objects.create(
            name=request.data['name'],
            description =request.data['description'],
            phone_number = request.data['phone_number'],
            is_alive = request.data['is_alive'],
            amount = request.data['amount'],
        )
        
        #RETURNING THE DATA TO THE FRONTEND
        return JsonResponse({"data":SimpleSerializer(new_test_content).data})
        
       
    
    def get(self, request):
        content =TestModel.objects.all().values()
        return JsonResponse({"data":SimpleSerializer(content,many=True).data})