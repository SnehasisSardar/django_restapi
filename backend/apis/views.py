# from django.shortcuts import render
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict  # Used later in the code
from django.views.decorators.csrf import csrf_exempt
from product.models import Product

# Create your views here.
@csrf_exempt
def api_home(request,*args,**kwargs):
    model_data=Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        # data['id']=model_data.id
        # data['title']=model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.price

        data = model_to_dict(model_data) # Used for the same purpuse as the above 4 lines
    return JsonResponse(data)