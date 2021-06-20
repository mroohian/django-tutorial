from django.urls import path

from .views import product_list, product_info

app_name='api'
urlpatterns = [
  path('v1/products', product_list),
  path('v1/products/<int:id>', product_info),
]
