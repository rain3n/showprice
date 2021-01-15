from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Product, ProductImage
from django.db.models.signals import post_save


@receiver(post_save, sender=Product)
def create_product(sender, instance, created, **kwargs):
    if created:
        ProductImage.objects.create(product = instance)


@receiver(post_save, sender=Product)
def save_product_profile(sender, instance, **kwargs):
    instance.productimage.save()





