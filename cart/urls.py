from django.urls import path, include
from .views import AddToCartView

urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
]
