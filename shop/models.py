from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import SellerProfile, BuyerProfile
from django.urls import reverse
from PIL import Image

class Product(models.Model):
    productName = models.CharField(max_length=50, null=False, default='')
    productPrice = models.IntegerField(null=False, default=0)
    productDesc = models.TextField()
    productSpecs = models.TextField()
    productTags = models.CharField(max_length=100, null=False, default='')
    productStocks = models.IntegerField(null=False, default=0)
    productPosted = models.DateTimeField(default = timezone.now)
    store = models.ForeignKey(SellerProfile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.productName

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk })


class ProductImage(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    image = models.ImageField(default = 'product_default.jpg', upload_to='product_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
            
        if img.height > 350 or img.width > 400:
            output_size = (400,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def __str__(self):
        return f'{self.product.productName} Image'

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk })

class Order(models.Model):
    buyer = models.ForeignKey(BuyerProfile, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)      

    def __str__(self):
        return self.id


class ReserveAddress(models.Model):
    customer = models.ForeignKey(BuyerProfile, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.buyername} Reserve'