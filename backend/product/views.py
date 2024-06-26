from rest_framework import authentication,generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from apis.authentication import TokenAuthentication
from apis.mixins import StaffEditorPermissionMixin
from .models import Product
from .serializers import ProductSerializer
from apis.permissions import IsStaffEditorPermission

class ProductDetailsAPIView(generics.RetrieveAPIView,StaffEditorPermissionMixin):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication,TokenAuthentication] 
    # Added the default in the settings of cfehome
    # permission_classes= [permissions.IsAdminUser,IsStaffEditorPermission] # Added via mixins

    def perform_create(self,serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


class ProductUpdateAPIView(generics.UpdateAPIView,StaffEditorPermissionMixin):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes= [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            # #

class ProductDeleteAPIView(generics.DestroyAPIView,StaffEditorPermissionMixin):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes= [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_destroy(self,instance):
        super().perform_destroy(instance)

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,StaffEditorPermissionMixin):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes= [permissions.IsAdminUser, IsStaffEditorPermission]
    lookup_field= 'pk'

    def get(self, request, *args, **kwargs):
        # print(args,kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validate_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

    def put(self,request, *args, **kwargs):
        pk= kwargs.get("pk")
        if pk is not None:
            return self.update(request, *args, **kwargs)

    # def perform_update(self, serializer):
    #     instance= serializer.save()
    #     # if not instance.content:
        #     instance.content = instance.title

    def delete(self,request, *args, **kwargs):
        pk= kwargs.get("pk")
        if pk is not None:
            return self.destroy(request, *args, **kwargs)



@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method  
    pk=kwargs.get("pk") #If using this no need to put pk=None
    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all() 
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)