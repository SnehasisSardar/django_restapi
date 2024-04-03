# from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product.models import Product

# Create your views here.
@csrf_exempt
def api_home(request,*args,**kwargs):
    model_data=Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        data['id']=model_data.id
        data['title']=model_data.title
        data['content']=model_data.content
        data['price']=model_data.price
    return JsonResponse(data)