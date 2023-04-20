from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def simple(request):
    method = request.method.lower()
    if method == 'get':
        return JsonResponse({"data":[1,2,3,4,5]})
    elif method == 'post':
        return JsonResponse({"data":"Added successfully"})
    elif method == 'put':
        return JsonResponse({"data":"Updated successfully"})
    return JsonResponse({"error":"Method not allowed"})