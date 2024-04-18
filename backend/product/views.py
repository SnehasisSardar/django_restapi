from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductDetailsAPIView(generics.RetrieveAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            # #

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self,instance):
        super().perform_destroy(instance)

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self,serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validate_get('content')or None
        if content is None:
            content = title

        serializer.save(content=content)