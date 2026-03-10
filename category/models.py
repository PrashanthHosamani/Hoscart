from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=15, unique=True)
    description = models.TextField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='photos/categories', blank=True)
    created_at = models.DateTimeField( )
    updated_at = models.DateTimeField()
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        
    
    def __str__(self):
        return self.name
    
    


    
    
    
    
    