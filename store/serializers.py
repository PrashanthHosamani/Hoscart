from rest_framework import serializers
from . models import Product
from category.serializers import CategorySmallSerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySmallSerializer()
    class Meta:
        model = Product
        fields = ['product_name', 'id', 'stock', 'image', 'price', 'description', 'is_available', 'category' ]
   
    