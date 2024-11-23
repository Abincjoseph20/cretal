from .models import Cart_items,Carts
from .views import _cart_id


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return{}
    else:
        try:
            cart = Carts.objects.filter(cart_id =_cart_id(request))
            if request.user.is_authenticated:
                cart_items = Cart_items.objects.filter(user=request.user)
            else:
                cart_items = Cart_items.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
                
        except Carts.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)