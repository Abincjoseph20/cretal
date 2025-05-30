from django.db import models
from mainapp.models import Product
from accounts.models import Account
# Create your models here.
                                                    #cart
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Carts(models.Model):
    cart_id = models.CharField(max_length=100,blank=True)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.cart_id

class Cart_items(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField()
    is_active =models.BooleanField(default=True)
    def sub_total(self):
        return self.product.discounted_price * self.quantity

    def __str__(self):
        return str(self.product)

                                                    #wishlist
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class wishlist(models.Model):
    wish_id = models.CharField(max_length=100,blank=True)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.wish_id


class wishlist_items(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    wish = models.ForeignKey(wishlist, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active =models.BooleanField(default=True)
    def sub_total(self):
        return self.product.discounted_price * self.quantity

    def __str__(self):
        return str(self.product)


                                                    #buynow
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class BuyNow(models.Model):
    buynow_id = models.CharField(max_length=100,blank=True)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.buynow_id


class BuyNow_items(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    buynow = models.ForeignKey(BuyNow, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active =models.BooleanField(default=True)
    def sub_total(self):
        return self.product.discounted_price * self.quantity

    def __str__(self):
        return str(self.product)
