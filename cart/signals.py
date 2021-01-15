from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Cart, CartItem
from shop import Product
from django.db.models.signals import post_save




  #  if created:
   #     CartItem.item_total = Product.productPrice * CartItem.quantity
#
 #       total = 0
  #      for item in CartItem:
   #         total += item.item_total
    #    
     #   CartItem.cart.cart_total = total
        