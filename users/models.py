from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
            
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f'{self.user.username} Profile'


class SProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
            
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f'{self.user.username} SProfile'


class BuyerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    buyerName = models.CharField(max_length=255)
    buyerAddress = models.CharField(max_length=255)
    buyerContactNumber = models.CharField(max_length = 11)

    def __str__(self):
        return f'{self.user.username} Buyer Profile'

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)


class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    storeName = models.CharField(max_length=255)
    storeAddress = models.CharField(max_length=255)
    storeContactNumber = models.CharField(max_length = 11, default = '')

    def __str__(self):
        return f'{self.storeName}'
    
    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)