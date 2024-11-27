from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from .models import Product

# Create your views here.

def base(request):
    products = Product.objects.all()
    print("Products:", products)  # Debugging
    return render(request, 'mainapp/home.html')


#locals() is a built in function to call all the local functions
class Category(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,'mainapp/category.html',locals())


class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,'mainapp/category.html',locals())


class ProductDetails(View):   
    def get(self, request,pk):
        # products = Product.objects.get(pk=pk)
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'mainapp/productdetais.html',{'products': product})


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product = Product.objects.order_by('-crated_date').filter(description__icontains=keyword)
            # product_count = product.count()
        else:
            return redirect('home')
    contxt = {
        'product' : product,
        # 'product_count' : product_count,
    }
    return render(request,'mainapp/store.html',contxt)


def store(request):
    product={
        'product':Product.objects.all()
    }
    return render(request,'mainapp/store.html',product)



def demo(request):
    return render(request,'mainapp/demo.html')