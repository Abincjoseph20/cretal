from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from .models import Product

# Create your views here.

# def base(request):
#     products = Product.objects.all()
#     for product in products:
#         print(f"Product ID: {product.id}")
#     return render(request, 'mainapp/home.html',{'products': products})


# #locals() is a built in function to call all the local functions
# class Category(View):
#     def get(self,request,val):
#         products = Product.objects.filter(category=val)
#         titles = Product.objects.filter(category=val).values('title')
#         context = {
#             'products': products,
#             'titles': titles,
#         }
#         return render(request,'mainapp/category.html',context)


# class CategoryTitle(View):
#     def get(self,request,val):
#         products = Product.objects.filter(title=val)
#         titles = Product.objects.filter(category=products[0].category).values('title')
#         context = {
#             'products': products,
#             'titles': titles,
#         }
#         return render(request,'mainapp/category.html',context)


# class ProductDetails(View):   
#     def get(self, request,pk):
#         # products = Product.objects.get(pk=pk)
#         product = get_object_or_404(Product, pk=pk)
#         print(f"Product Detail ID: {product.id}")  # Debugging
#         return render(request, 'mainapp/productdetais.html',{'products': product})


def base(request):
    products = Product.objects.all()
    context ={
        'products':products
    }
    return render(request,'mainapp/index.html',context)

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
            products = Product.objects.order_by('-created_date').filter(description__icontains=keyword)
            # product_count = product.count()
        else:
            return redirect('home')
    contxt = {
        'products' : products,
        # 'product_count' : product_count,
    }
    return render(request,'mainapp/store.html',contxt)


def store(request):
    products = Product.objects.all()
    contxt ={
        'products':products
    }
    return render(request,'mainapp/store.html',contxt)



def demo(request):
    return render(request,'mainapp/demo.html')


def erro_handiling(request):
    return render(request,'mainapp/error_message.html')