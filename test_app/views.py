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
        serializer.save()
        
        # # CREATING AND INSERTING THE NEW DATA
        # new_test_content=TestModel.objects.create(
        #     name=request.data['name'],
        #     description =request.data['description'],
        #     phone_number = request.data['phone_number'],
        #     is_alive = request.data['is_alive'],
        #     amount = request.data['amount'],
        # )
        
        #RETURNING THE DATA TO THE FRONTEND
        return JsonResponse({"data":serializer.data})
        
       
    
    def get(self, request):
        content =TestModel.objects.all().values()
        return JsonResponse({"data":SimpleSerializer(content,many=True).data})
    
    
    def put(self,request ,*args, **kwargs):
        model_id = kwargs.get("id",None)
        if not model_id:
            return JsonResponse({"error": "method /PUT/ not allowed"})
        
        try:
            instance=TestModel.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "Object does not exists"})
        
        serializer = SimpleSerializer(data=request.data,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})

                