from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    edit_url = serializers.HyperlinkedIdentityField(view_name="product-edit",lookup_field="pk")
    url=serializers.HyperlinkedIdentityField(view_name="product-detail",lookup_field="pk")
    class Meta:
        model = Product
        fields=[
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price'
        ]        

    # def get_edit_url(self,obj):
    #     # return f"/apis/v2/product/{obj.pk}/"
    #     request= self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("product-edit",kwargs={"pk":obj.pk}, request=request)
