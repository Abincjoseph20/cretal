from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [

    path('registration',views.Register,name='registration'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

]