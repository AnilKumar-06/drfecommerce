from rest_framework import viewsets
from rest_framework.response import Response
from drfecommerce.product.models import (Brand, Product, Category)
from drfecommerce.product.serializers import (BrandSerializer, ProductSerializer, CategorySerializer)

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework.decorators import action

class CategoryViewSet(viewsets.ViewSet):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    @action(
            detail=False,
            methods=['get'],
            url_path = r"(?P<category>\w+)/all"
    )
    def list_product_by_category(self, request, category=None):
        serialized = ProductSerializer(self.queryset.filter(category__name=category))
        return Response(serialized.data)

    @extend_schema(request=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
    

class BrandViewSet(viewsets.ViewSet):

    serializer_class = BrandSerializer
    @extend_schema(request=BrandSerializer)
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)

        return Response(serializer.data)
    

class ProductViewSet(viewsets.ViewSet):

    queryset = Product.objects.all()

   
    serializer_class = ProductSerializer
    @extend_schema(request=ProductSerializer)
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(self.queryset, many=True)

        return Response(serializer.data)