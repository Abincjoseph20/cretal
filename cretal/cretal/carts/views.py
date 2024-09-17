from django.shortcuts import render,redirect,get_object_or_404
from mainapp.models import Product
from .models import Carts,Cart_items,wishlist,wishlist_items
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def _cart_id(request): #this private function is using to fetch the session id of a single product
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
def add_to_cart(request,product_id): #to get the Product
    product = Product.objects.get(id=product_id)
    try:
        cart = Carts.objects.get(cart_id=_cart_id(request)) #get the cart id using the cart session
    except ObjectDoesNotExist:
        cart = Carts.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = Cart_items.objects.get(product=product,cart=cart) #if there is morethan one time add to a single product in cart the qty will incresse
        cart_item.quantity += 1 #expantion -> (cart_item.quantity = cart_item.quantity + 1)
        cart_item.save()

    except ObjectDoesNotExist: #if there is no Existing product here then add the product to the cart
        cart_item = Cart_items.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    # return HttpResponse(cart_item.quantity)
    # exit()
    return redirect('cart')

def Cart_view(request,total=0,quantity=0,cart_items=None):  # this function for view Cart page
    try:
        cart = Carts.objects.get(cart_id=_cart_id(request))
        cart_items = Cart_items.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.discounted_price * cart_item.quantity)
            quantity += cart_item.quantity
            # print(cart_items.quantity)
        tax = ( 2 * total)/100
        shipping = 4
        grand_total = total + tax + shipping
    except ObjectDoesNotExist:
        pass

    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,
        'shipping':shipping
    }
    return render(request, 'mainapp/cart.html', context)



def minus_cart(request,product_id):
    cart = Carts.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = Cart_items.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request,product_id):
    cart = Carts.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = Cart_items.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart')


# /////////////////////////////////////////////////////////////


# Helper function to fetch or create the session key for a wishlist
def _wished_id(request):
    wish = request.session.session_key
    if not wish:
        wish = request.session.create()
    return wish


# View to add a product to the wishlist
def wish_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        wish = wishlist.objects.get(wish_id=_wished_id(request))  # Get the wishlist using the session key
    except ObjectDoesNotExist:
        wish = wishlist.objects.create(wish_id=_wished_id(request))
    wish.save()

    try:
        wish_item = wishlist_items.objects.get(product=product,
                                               wish=wish)  # Check if the product is already in the wishlist
        wish_item.quantity += 1  # Increment quantity if the product is already in the wishlist
        wish_item.save()
    except ObjectDoesNotExist:
        wish_item = wishlist_items.objects.create(
            product=product,
            quantity=1,
            wish=wish,
        )
        wish_item.save()

    return redirect('wish')  # Redirect to the wishlist view


# View to display the wishlist
def wish_view(request, total=0, quantity=0, wish_item=None):
    try:
        wish = wishlist.objects.get(wish_id=_wished_id(request))  # Get the wishlist using the session key
        wish_item = wishlist_items.objects.filter(wish=wish, is_active=True)
        for item in wish_item:
            total += (item.product.discounted_price * item.quantity)  # Calculate total price
            quantity += item.quantity  # Calculate total quantity
        tax = (2 * total) / 100
        shipping = 4
        grand_total = total + tax + shipping
    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'wish_item': wish_item,
        'tax': tax,
        'grand_total': grand_total,
        'shipping': shipping
    }
    return render(request, 'mainapp/wishlist.html', context)


# View to remove a product from the wishlist
def remove_wish_item(request, product_id):
    wish = wishlist.objects.get(wish_id=_wished_id(request))  # Get the wishlist using the session key
    product = get_object_or_404(Product, id=product_id)
    wish_item = wishlist_items.objects.get(product=product, wish=wish)
    wish_item.delete()
    return redirect('wish')  # Redirect to the wishlist view
