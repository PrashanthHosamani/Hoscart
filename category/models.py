from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=15, unique=True)
    description = models.TextField(max_length=255, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='photos/categories', blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        
    def get_url(self):
            return reverse('products_by_category', args = [self.slug])
    
    def __str__(self):
        return self.category_name
    

    
    


    
    
    
    
    