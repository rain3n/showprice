from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, BuyerProfile, SProfile, SellerProfile
from cart.models import Cart


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        BuyerProfile.objects.create(user=instance)
        SProfile.objects.create(user=instance)
        SellerProfile.objects.create(user=instance)
        Cart.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

