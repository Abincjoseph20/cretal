from django.urls import path
from . import views
# from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.Cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('minus_cart/<int:product_id>/', views.minus_cart, name='minus_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart_item, name='remove_cart'),

]