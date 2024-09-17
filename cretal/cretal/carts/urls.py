from django.urls import path
from . import views
# from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.Cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('minus_cart/<int:product_id>/', views.minus_cart, name='minus_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart_item, name='remove_cart'),

# {% url 'remove_cart' cart_item.product.id %}

    path('wish', views.wish_view, name='wish'),
    path('wish_to_cart/<int:product_id>/', views.wish_to_cart, name='wish_to_cart1'),
    path('remove_wish_item/<int:product_id>/', views.remove_wish_item, name='remove_wish_item'),

]