from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView

class simple(APIView):
    def post(self, request):
        return JsonResponse({"data":[1,2,3,4,5]})
    
    def get(self, request):
        return JsonResponse({"data":[1,2,3,4]})