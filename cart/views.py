from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_list_or_404, get_object_or_404
from users.models import BuyerProfile
from .models import Cart, CartItem
from django.contrib.auth.models import User

def test(request):
    return render(request, "cart/base.html")


##-------------- Cart Views --------------------------------------

class DetailCart(DetailView):
    model = Cart
    template_name='cart/detail_cart.html'


##-------------- CartItem Views --------------------------------------


class ListCartItem(LoginRequiredMixin, ListView):
    model = CartItem
    context_object_name = 'cartitems'
    template_name='cart/list_cartitems.html'
    allow_empty = True

    def get_queryset(self):
        mycart = get_object_or_404(Cart, user=self.request.user)
        return CartItem.objects.filter(cart=mycart)


class CreateCartItem(LoginRequiredMixin, CreateView):
    model = CartItem
    fields = ['quantity']
    template_name = 'cart/create_cartitem.html'

    #def dispatch(self, request, *args, **kwargs):
    #    """
   #    Overridden so we can make sure the `Ipsum` instance exists
    #    before going any further.
     #   """
    #    self.product = get_object_or_404(product, pk=kwargs['product_id'])
   #     return super().dispatch(request, *args, **kwargs)

   # def form_valid(self, form):
   #     form.instance.user = self.request.user
  #      form.instance.product = self.product
 #       return super().form_valid(form)



class DeleteCartItem(DeleteView):
    model = Cart
    template_name = 'cart/delete_cartitem.html'


