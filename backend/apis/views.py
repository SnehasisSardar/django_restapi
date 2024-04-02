# from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def api_home(request,*args,**kwargs):
    print(request.GET)
    body=request.body #byte string of JSON data
    data={}
    try:
        data=json.loads(body) #string of JSON data -> python dict
    except:
        pass
    print(data)
    print(request.headers)
    data['headers']=dict(request.headers)
    data['content_type']=request.content_type
    return JsonResponse(data)