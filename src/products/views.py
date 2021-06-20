from django.shortcuts import render, get_object_or_404

from products.models import Product

# Create your views here.
def product_list_view(request):
  products = Product.objects.all()
  context = {
    'title': 'Products list',
    'products': products
  }

  return render(request, 'products/list.html', context)

def product_detils_view(request,id):
  product = get_object_or_404(Product, id=id)
  context = {
    'title': product.title,
    'product': product
  }

  return render(request, 'products/details.html', context)