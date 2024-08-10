from django.db import models
from mainapp.models import Product
# Create your models here.

class Carts(models.Model):
    cart_id = models.CharField(max_length=100,blank=True)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.cart_id


class Cart_items(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active =models.BooleanField(default=True)
    def sub_total(self):
        return self.product.discounted_price * self.quantity


    def __str__(self):
        return self.product