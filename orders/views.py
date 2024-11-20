from django.shortcuts import render,redirect
from django.http import HttpResponse
from carts.models import Cart_items
from .forms import OrderForms
from .models import Order
import datetime
# Create your views here.

def place_orders(request,total=0, quantity=0):
    current_user =  request.user
    
    #if the cart count is <= 0 redirect to the store page
    Cart_item = Cart_items.objects.filter(user=current_user)
    cart_count = Cart_item.count()
    if cart_count <= 0:
        return redirect('store')
    
    grand_total = 0
    tax = 0
    shipping = 0
    
    for cart_item in cart_item:
            total += (cart_item.product.discounted_price * cart_item.quantity)
            quantity += cart_item.quantity
    tax = (2 * total) / 100
    shipping = 4
    grand_total = total + tax + shipping
    
    
    if request.method == 'POST':
        form = OrderForms(request.POST)
        if form.is_valid():
            #store all billing details in side order
            data = Order()
            data.first_name = form.cleaned_data('first_name')
            data.last_name = form.cleaned_data('last_name')
            data.phone = form.cleaned_data('phone')
            data.email = form.cleaned_data('email')
            data.address_line1 = form.cleaned_data('address_line1')
            data.address_line2 = form.cleaned_data('address_line2')
            data.country = form.cleaned_data('country')
            data.state = form.cleaned_data('state')
            data.city = form.cleaned_data('city')
            data.order_note = form.cleaned_data('forder_note')
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('EREMOTE_ADDAR')
            data.save()
            #genarate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.data.today().strftime('%d'))
            mt = int(datetime.data.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
            return redirect('/')
    else:
        return redirect('/')