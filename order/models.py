from django.db import models
from accounts.models import Account
from cart.models import Cart
from store.models import Product


class Order(models.Model):
    user = models.ForeignKey(Account, related_name ='orders', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    status_choices = [
        ("PENDING", "pending"),
        ("PAID", "paid"),
        ("CANCELLED", "cancelled"),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default="PENDING")
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)