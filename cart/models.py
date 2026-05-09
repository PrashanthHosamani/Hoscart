from django.db import models
from django.core.validators import MinValueValidator
from store.models import Product
from accounts.models import Account


class Cart(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}'s Cart"


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.product.product_name} ({self.quantity})"

    class Meta:
        unique_together = ('cart', 'product')