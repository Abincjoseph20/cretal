from django.urls import path
from . import views
# from django.contrib.auth import views as auth_view


urlpatterns = [

     path('place_order/', views.place_orders, name='place_orders'),
     path('payments/',views.payments,name='payments'),
     path('order_completed/',views.order_completed,name='order_completed')
]