from django.contrib import admin
from . models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("products_name", "price", "stock", "category", "updated_date", "is_available",)
    prepopulated_fields = {"slug" : ("products_name",)}

admin.site.register(Product, ProductAdmin)




