from django.shortcuts import render,redirect
from django.http import HttpResponse
from carts.models import Cart_items
from .forms import OrderForms
from .models import Order,Payment,OrderProduct
import datetime
import json
# Create your views here.

def place_orders(request,total=0, quantity=0):
    current_user =  request.user
    
    #if the cart count is <= 0 redirect to the store page
    cartitems = Cart_items.objects.filter(user=current_user)
    cart_count = cartitems.count()
    if cart_count <= 0:
        return redirect('store')
    
    grand_total = 0
    tax = 0
    shipping = 0
    
    for cart_item in cartitems:
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
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line1 = form.cleaned_data['address_line1']
            data.address_line2 = form.cleaned_data['address_line2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note'] 
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR') 
            data.save()
            #genarate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d')) 
            mt = int(datetime.date.today().strftime('%m')) 
            d = datetime.date(yr,mt,dt)
            # current_date = d.strftime("%y%m%d")
            current_date = d.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
            
            
            
            order = Order.objects.get(user=current_user,is_ordered=False,order_number=order_number)
            context ={
                'order':order,
                'cart_items':cartitems,
                'total':total,
                'tax':tax,
                'grand_total': grand_total,
                'shipping': shipping
            }
            # return redirect('check_out')
            return render(request,'orders/payments.html',context)
            
        else:
            print(form.errors)
            return redirect('check_out')
    else:
        form = OrderForms()
        return render(request, 'orders/payments.html', {
            'form': form, 
            'cart_items': cartitems, 
            'grand_total': grand_total, 
            'tax': tax, 
            'shipping': shipping
            })
        
        

def payments(request):
    body = json.loads(request.body)
    order = Order.objects.get(user=request.user,is_ordered=False,order_number=body['orderID'])
    
    # print(body)
    payment = Payment(
        user = request.user,  
        payment_id=body['transID'],
        payment_method=body['payment_method'], 
        amount_paid = order.order_total,
        status = body['status'],
    )
    payment.save()
    
    order.payment=payment
    order.is_ordered=True
    order.save()
    
    # move the cart item to order Product

    cartitems = Cart_items.objects.filter(user=request.user)
    for item in cartitems:
        orderproduct = OrderProduct()
        orderproduct.order_id = order.id
        orderproduct.payment = payment
        orderproduct.user_id = request.user.id
        orderproduct.product_id = item.product_id
        orderproduct.quantity = item.quantity
        orderproduct.product_price = item.product.discounted_price
        orderproduct.size = 'Default Size'
        orderproduct.ordered = True
        orderproduct.save()
        
    return render(request,'orders/payments.html')

