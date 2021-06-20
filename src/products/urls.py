from django.urls import path
from mydjango.urls import make_redirect

from products.views import product_list_view, product_detils_view

app_name='products'
urlpatterns = [
    path('', make_redirect('list/')),
    path('list/', product_list_view, name='product-list'),
    path('<int:id>', product_detils_view, name='product-details'),
]
