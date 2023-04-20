from django.http import JsonResponse, response

def simple(request):
    
    return response.HttpResponse("Welcome home")