from django.urls import path
from . import views
from .views import (
    ListCartItem,
    CreateCartItem
)

urlpatterns = [

    path('cart/test/', views.test, name='test'),
    path('cart/', views.ListCartItem.as_view(), name='my-cart'),
    path('product/<int:product_id>/add',views.CreateCartItem.as_view(), name = 'create-carrtitem'),

]
