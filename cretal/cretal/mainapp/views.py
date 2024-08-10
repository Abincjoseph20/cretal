from django.shortcuts import render,redirect
from django.views import View
from .models import Product

# Create your views here.

def base(request):
    return render(request,'mainapp/home.html')

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
        product = Product.objects.get(pk=pk)
        return render(request, 'mainapp/productdetais.html', locals())


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