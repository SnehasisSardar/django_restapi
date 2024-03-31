# from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def api_home(request,*args,**kwargs):
    body=request.body #byte string of JSON data
    print(body)
    return JsonResponse({"message":"Hi there, This the Django API response you were looking for"})