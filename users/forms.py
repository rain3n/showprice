from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, BuyerProfile, SellerProfile, SProfile


class UserRegisterForm(UserCreationForm):

    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username',}),
            'email': forms.EmailInput(attrs={'placeholder':'Email',}),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update({'placeholder':('Password')})
        self.fields['password2'].widget.attrs.update({'placeholder':('Confirm Password')})

        for fieldname in ['username', 'password1', 'password2', 'email']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = "ㅤ"
            self.fields[fieldname].label_suffix = " "
    
   
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
                 'placeholder':'Username',
                 })

        self.fields['password'].widget.attrs.update({
                 'placeholder':'Password',
                 })

        for fieldname in ['username', 'password']:
            self.fields[fieldname].label = "ㅤ"
            self.fields[fieldname].label_suffix = " "   


class UserUpdateForm(forms.ModelForm): 
    email = forms.EmailInput()
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Email Address"


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = SProfile 
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Profile Picture"


class SProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(SProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Store Profile Picture"



class BuyerUpdateForm(forms.ModelForm):

    buyerName = forms.CharField(label='Full Name',max_length= 255)
    buyerAddress = forms.CharField(label='Address',max_length= 255)
    buyerContactNumber = forms.CharField(label = 'Contact Number', max_length=11)

    class Meta:
        model = BuyerProfile
        fields = ['buyerName','buyerAddress', 'buyerContactNumber']


class SellerUpdateForm(forms.ModelForm):

    storeName = forms.CharField(label='Store Name',max_length= 255)
    storeAddress = forms.CharField(label='Store Address',max_length= 255)
    storeContactNumber = forms.CharField(label = 'Store Contact Number', max_length=11)

    class Meta:
        model = SellerProfile
        fields = ['storeName','storeAddress', 'storeContactNumber']