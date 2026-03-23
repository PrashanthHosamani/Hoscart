from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    slug = models.SlugField(max_length=100, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.category_name
    

    
    


    
    
    
    
    