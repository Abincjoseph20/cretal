from django.contrib import admin
from .models import Carts,Cart_items,wishlist,wishlist_items,BuyNow,BuyNow_items
# Register your models here.

admin.site.register(Carts)
admin.site.register(Cart_items)

admin.site.register(wishlist)
admin.site.register(wishlist_items)


admin.site.register(BuyNow)
admin.site.register(BuyNow_items)
