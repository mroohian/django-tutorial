from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField(blank=True, null=True)
  price = models.DecimalField(max_digits=100, decimal_places=2)
  summary = models.TextField()
  feature = models.BooleanField()

  def get_list_url(self):
    return reverse('products:product-list')

  def get_absolute_url(self):
    return reverse('products:product-details', kwargs={'id': self.id})
