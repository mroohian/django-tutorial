from django.shortcuts import get_object_or_404
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def product_list(request):
  products = Product.objects.all()
  serializer = ProductSerializer(products, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def product_info(request, id):
  product = get_object_or_404(Product, id=id)
  serializer = ProductSerializer(product)
  return Response(serializer.data)
