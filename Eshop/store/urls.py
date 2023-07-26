from django.contrib import admin
from django.urls import path
from store import views
from .views import Login,SignUp, Index,cart,checkout,order


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup',SignUp.as_view(), name='signup'),
    path('login',Login.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
    path('cart',cart.as_view(),name='cart'),
    path('checkout',checkout.as_view(),name='checkout'),
    path('order',order.as_view(),name='order')
]