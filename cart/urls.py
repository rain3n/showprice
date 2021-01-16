from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('cart/test/', views.test, name='test'),
    path('cart/', views.ListCartItem.as_view(), name='my-cart'),
    path('cart/checkout', views.Checkout.as_view(), name='checkout'),

]
