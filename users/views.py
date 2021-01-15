from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, BuyerUpdateForm, SProfileUpdateForm, SellerUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #messages.success(request, f'Account Created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)


@login_required
def buyer_profile(request):
    if request.method == 'POST':
        bp_form = BuyerUpdateForm(request.POST, instance=request.user.buyerprofile)

        if bp_form.is_valid():
            bp_form.save()
            return redirect('buyer-profile')

    else:
        bp_form = BuyerUpdateForm(instance=request.user.buyerprofile)

    context = {
        'bp_form': bp_form,
    }

    return render(request, 'users/buyer.html', context)


@login_required
def seller_profile(request):
    if request.method == 'POST':
        s_form = SellerUpdateForm(request.POST, instance=request.user.sellerprofile)
        sp_form = SProfileUpdateForm(request.POST, request.FILES, instance=request.user.sprofile)

        if s_form.is_valid() and sp_form.is_valid():
            s_form.save()
            sp_form.save()
            return redirect('seller-profile')
    else:
        s_form = SellerUpdateForm(instance=request.user.sellerprofile)
        sp_form = SProfileUpdateForm(instance=request.user.sprofile)

    context = {
        's_form': s_form,
        'sp_form': sp_form,
    }

    return render(request, 'users/seller.html', context)


#@login_required
#def profile(request):
#    if request.method == 'POST':
#        bp_form = BuyerProfileUpdateForm(request.POST, instance=request.user)
        
#        if bp_form.is_valid():
#            bp_form.save()
#            messages.success(request, f'Your Account Has Been Updated!')
#            return redirect('profile')

#    else:
#        bp_form = ProfileUpdateForm(instance=request.user)
        
#    context = {
#        'bp_form': bp_form,
#    }

#    return render(request, 'users/profile.html', context)