from django.contrib import admin
from .models import Profile, BuyerProfile, SellerProfile, SProfile

admin.site.register(Profile)
admin.site.register(SProfile)
admin.site.register(BuyerProfile)
admin.site.register(SellerProfile)
