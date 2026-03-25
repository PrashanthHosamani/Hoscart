from django.db import models
from category.models import Category

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length = 200, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="photos/products")
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.product_name
    
    @property
    def is_available(self):
        return self.stock > 0
    
    