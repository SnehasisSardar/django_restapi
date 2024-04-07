# from django.shortcuts import render

import json
from django.http import JsonResponse
from django.forms.models import model_to_dict  # Used later in the code
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view

from product.models import Product
from product.serializers import ProductSerializer

# Create your views here.
@api_view(["POST"])
@csrf_exempt
def api_home(request,*args,**kwargs):
    serializer=ProductSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        # instance=serializer.save()
        print(serializer.data)
    
        return Response(serializer.data)