from django.urls import path, include
from .views import AddToCartView, UpdateCartItem

urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('update-cart-item/<int:pk>/', UpdateCartItem.as_view(), name = 'update-cart-item'),
]
