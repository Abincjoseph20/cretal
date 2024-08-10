from django.urls import path
from . import views


urlpatterns = [
    path('',views.base,name='home'),
    path('categories/<slug:val>', views.Category.as_view(), name="category"),
    path('categories-title/<val>', views.CategoryTitle.as_view(), name="category-title"),
    path('ProductDetais/<int:pk>/', views.ProductDetails.as_view(), name='Product_detais'),
    path('search', views.search, name='search'),
    path('store/', views.store, name='store'),

]