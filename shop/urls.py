from django.urls import path
from . import views
from .views import *
 
urlpatterns = [
    #path('', ProductListView.as_view(), name='shop-home'),
    path('', views.product_query, name='shop-home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('product/<int:pk>/img/add/', ProductImageCreateView.as_view(), name='product-add-image'),
    path('product/<int:pk>/img/update/', ProductImageUpdateView.as_view(), name='product-update-image'),
    path('shops/<str:storename>/', ShopListView.as_view(), name='shop-list'),
    path('update_item/', views.updateItem, name="update_item"),
    path('search/', views.product_query, name='search'),
]
