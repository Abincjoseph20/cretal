from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='home'),
    path('demo', views.demo, name='demo1'),
    path('categories/<slug:val>', views.Category.as_view(), name="category"),
    path('categories-title/<val>', views.CategoryTitle.as_view(), name="category-title"),
    path('ProductDetails/<int:pk>/', views.ProductDetails.as_view(), name='Product_details'),  # Corrected here
    path('search', views.search, name='search'),
    path('store/', views.store, name='store'),
]

