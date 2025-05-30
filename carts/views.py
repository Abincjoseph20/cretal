from django.shortcuts import render, redirect, get_object_or_404
from mainapp.models import Product
from .models import Carts, Cart_items, wishlist, wishlist_items,BuyNow,BuyNow_items
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required




                                                    #cart
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



def _cart_id(request): # This private function is used to fetch the session id of a single product
    if request.user.is_authenticated:
        return request.user.id
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_to_cart(request, product_id): # To get the Product
    product = Product.objects.get(id=product_id)
    try:
        cart = Carts.objects.get(cart_id=_cart_id(request)) # Get the cart id using the cart session
    except ObjectDoesNotExist:
        cart = Carts.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()

    try:
        cart_item = Cart_items.objects.get(product=product, cart=cart) # If there is more than one time add to a single product in cart the qty will increase
        cart_item.quantity += 1 # Expansion -> (cart_item.quantity = cart_item.quantity + 1)
        cart_item.save()
    except ObjectDoesNotExist: # If there is no existing product here then add the product to the cart
        cart_item = Cart_items.objects.create(
            product=product,
            quantity=1,
            cart=cart,
            user=request.user if request.user.is_authenticated else None
        )
        cart_item.save()
    return redirect('cart')

def Cart_view(request, total=0, quantity=0, cart_items=None):  # This function for viewing Cart page
    try:
        if request.user.is_authenticated:
             cart_items = Cart_items.objects.filter(user=request.user, is_active=True)
        else:
            cart = Carts.objects.get(cart_id=_cart_id(request))
            cart_items = Cart_items.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.discounted_price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total) / 100
        shipping = 4
        grand_total = total + tax + shipping
    except ObjectDoesNotExist:
        tax = 0
        shipping = 0
        grand_total = 0

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
        'shipping': shipping
    }
    return render(request, 'mainapp/cart.html', context)


def minus_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_items = []
    try:
        if request.user.is_authenticated:
            cart_items = Cart_items.objects.filter(product=product, user=request.user.id, is_active=True)
        else:
            cart = Carts.objects.get(cart_id=_cart_id(request))
            cart_items = Cart_items.objects.filter(product=product, user=request.user.id, cart=cart, is_active=True)
            
        for cart_item in cart_items:   
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
    except ObjectDoesNotExist:
        pass
    return redirect('cart')

def remove_cart_item(request, product_id):
    
    product = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = Cart_items.objects.get(product=product, user=request.user)
        else:
            cart = Carts.objects.get(cart_id=_cart_id(request))
            cart_item = Cart_items.objects.get(product=product, cart=cart)
        cart_item.delete()
    except ObjectDoesNotExist:
        pass
    return redirect('cart')


                                                    #wishlist
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





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
        wish_item = wishlist_items.objects.get(product=product, wish=wish)  # Check if the product is already in the wishlist
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
        tax = 0
        shipping = 0
        grand_total = 0

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







                                                    #buynow
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def _buynow_id(request):  # This private function is used to fetch the session id of a single product
    buynow = request.session.session_key
    if not buynow:
        buynow = request.session.create()
    return buynow

def buynow_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    # Get or create a BuyNow instance for the current session
    buynow_id = _buynow_id(request)  # Retrieve the session key
    buynow, created = BuyNow.objects.get_or_create(buynow_id=buynow_id)
    # If a BuyNow instance with the given buynow_id exists, it is returned
    # If it does not exist, a new BuyNow instance is created and returned

    # Clear all existing items in the BuyNow cart
    BuyNow_items.objects.filter(buynow=buynow).delete()

    # Create a new BuyNow_items entry with the selected product
    buynow_item = BuyNow_items.objects.create(
        product=product,
        quantity=1,
        buynow=buynow
    )

    # Save the new BuyNow_items entry
    buynow_item.save()

    # Redirect to the buynow view
    return redirect('buynow')



def Buynow_view(request, total=0, quantity=0, buynow_items=None):  # This function for viewing Cart page
    try:
        buynow = BuyNow.objects.get(buynow_id=_buynow_id(request))
        buynow_items = BuyNow_items.objects.filter(buynow=buynow, is_active=True)
        for buynow_item in buynow_items:
            total += (buynow_item.product.discounted_price * buynow_item.quantity)
            quantity += buynow_item.quantity
        tax = (2 * total) / 100
        shipping = 4
        grand_total = total + tax + shipping
    except ObjectDoesNotExist:
        tax = 0
        shipping = 0
        grand_total = 0

    context = {
        'total': total,
        'quantity': quantity,
        'buynow_items': buynow_items,
        'tax': tax,
        'grand_total': grand_total,
        'shipping': shipping
    }
    return render(request, 'mainapp/buynow.html', context)

def minus_buynow_item(request, product_id):
    buynow = BuyNow.objects.get(buynow_id=_buynow_id(request))
    product = get_object_or_404(Product, id=product_id)
    buynow_item = BuyNow_items.objects.get(product=product,buynow=buynow)
    if buynow_item.quantity > 1:
        buynow_item.quantity -= 1
        buynow_item.save()
    else:
        buynow_item.delete()
    return redirect('buynow')

def remove_buynow_item(request, product_id):
    buynow = BuyNow.objects.get(buynow_id=_buynow_id(request))
    product = get_object_or_404(Product, id=product_id)
    buynow_item = BuyNow_items.objects.get(product=product, buynow=buynow)
    buynow_item.delete()
    return redirect('buynow')



@login_required
def check_out(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Carts.objects.get(cart_id=_cart_id(request))
        cart_items = Cart_items.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.discounted_price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total) / 100
        shipping = 4
        grand_total = total + tax + shipping
    except ObjectDoesNotExist:
        tax = 0
        shipping = 0
        grand_total = 0

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
        'shipping': shipping
    }
    return render(request, 'mainapp/checkout.html',context)

    
    