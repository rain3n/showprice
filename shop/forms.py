from .models import ProductImage
from django import forms


class ProductImageUpdateForm(forms.ModelForm):
    class Meta:
        model =  ProductImage
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(ProductImageUpdateForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Product Image"


class PImageUpdateForm(forms.ModelForm):
    class Meta:
        model =  ProductImage
        fields = ['image']