from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
import json

from users.models import SellerProfile, SProfile

from .forms import PImageUpdateForm
from .models import Product, ProductImage, Order
from cart.models import *


class ProductListView(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'
    ordering = ['-productPosted']
    paginate_by = 9


class ShopListView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        shop = get_object_or_404(SellerProfile, storeName=self.kwargs.get('storename'))
        return Product.objects.filter(store=shop).order_by('-productPosted')


class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = [ 'productName', 'productPrice', 'productDesc', 'productSpecs', 'productStocks', 'productTags']

    def form_valid(self,form):
        form.instance.store = self.request.user.sellerprofile
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = [ 'productName', 'productPrice', 'productDesc', 'productSpecs', 'productStocks']

    def form_valid(self, form):
        form.instance.store = self.request.user.sellerprofile
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user.sellerprofile == product.store:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        if self.request.user.sellerprofile == product.store:
            return True
        return False


class ProductImageCreateView(LoginRequiredMixin, CreateView):
    model = ProductImage
    fields = ['image']

    def form_valid(self, form):
        form.instance.store = self.request.user.sellerprofile
        return super().form_valid(form)


class ProductImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ProductImage
    fields = ['image']

    def form_valid(self, form):
        form.instance.store = self.request.user.sellerprofile
        return super().form_valid(form)

    def test_func(self):
        productp = self.get_object()
        if self.request.user.sellerprofile == productp.product.store:
            return True
        return False

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    product = Product.objects.get(id = productId)

    order, created = Order.objects.get_or_create(buyer=request.user.buyerprofile, complete=False)    
    cartitem, created = CartItem.objects.get_or_create(cart=request.user.cart, product=product)

    if action == 'add':
        if cartitem.quantity < product.productStocks:
            cartitem.quantity += 1
    elif action == 'remove':
        cartitem.quantity -= 1
    elif action == 'remove-all':
        cartitem.quantity = 0
    
    cartitem.save()

    if cartitem.quantity <=0:
        cartitem.delete()

    return JsonResponse('Item was added', safe=False)


def product_query(request):
    
    querylist = request.GET.getlist('q')
    if querylist:
        query = querylist[0]
        budget = querylist[1]
        qs = Product.objects.all().order_by('-productPrice')
    else:
        query = ""
        budget = ""
        qs = Product.objects.all().order_by('-id')
    if query:
        qs = qs.filter(
            Q(productName__icontains=query) |
#           Q(productDesc__icontains=query) |
#           Q(productSpecs__icontains=query)|
            Q(productTags__icontains=query) |
            Q(store__storeName__icontains=query)
        )
    if budget:
       qs = list(chain(
            qs.filter(productPrice__lte=budget),
            qs.filter(productPrice__gt=budget).order_by('productPrice'),
            ))
           
    paginate = Paginator(qs, 9)
    page = request.GET.get('page')    

    try:
        qs = paginate.page(page)
    except PageNotAnInteger:
        qs = paginate.page(1)
    except EmptyPage:
        qs = paginate.page(paginate.num_pages)

    context = {
        "products": qs,
    }
    template = "shop/home.html"

    return render(request, template, context)
    