from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Cart, CartItem
from shop import Product
from django.db.models.signals import post_save