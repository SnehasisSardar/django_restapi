# from django.shortcuts import render

import json
from django.http import JsonResponse
from django.forms.models import model_to_dict  # Used later in the code
from django.views.decorators.csrf import csrf_exempt

# from rest_framework.response import Response
# from rest_framework.decorators import api_view

from product.models import Product
from product.serializers import ProductSerializer

# Create your views here.
# @api_view(["GET"])
@csrf_exempt
def api_home(request,*args,**kwargs):
    instance=Product.objects.all().order_by("?").first()
    data={}
    if instance:  
        # data['id']=model_data.id
        # data['title']=model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.price

        # data = model_to_dict(instance,fields=['id','title','content','price','sale_price']) # Used for the same purpuse as the above 4 lines
        data= ProductSerializer(instance).data
    return JsonResponse(data)
    # return Response(data)