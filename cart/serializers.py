from rest_framework import serializers
from . models import CartItem, Cart
from store.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity', 'total_price']
        
    def get_total_price(self, obj):
        return obj.product.price * obj.quantity
    

class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
        
    #custom validation to check if the product exists and its quantity is not less then 1
    def validate(self, data):
        product_id = data.get('product_id')
        quantity = data.get('quantity')
        
        #check if the product exists or not 
        try:
            product = Product.objects.get(id = product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product Not Found")
        
        #quantity validation
        if quantity < 1:
            raise serializers.ValidationError("Quantity must be greater then 0")
        
        #stock validation against the quantity, if the quantity entered by user is greater then the stock 
        if product.stock < quantity:
            raise serializers.ValidationError(
                f" Only {product.stock} items remaining in stock."
            )
        
        data["product"] = product
        return data
     
    def create(self, validated_data):
        request = self.context["request"]
        user = request.user
        
        product =validated_data["product"]
        quantity = validated_data["quantity"] 
        
        #get if the cart is already created or exist or create if not
        cart, _ = Cart.objects.get_or_create(user=user)
        
        try:
            cart_item = CartItem.objects.get(cart = cart, product = product)
            
            new_quantity = cart_item.quantity + quantity
            
            if new_quantity > product.stock:
                raise serializers.ValidationError(
                    f"Only {Product.stock} items available"
                    )
            cart_item.quantity = new_quantity
            cart_item.save()
     
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                cart = cart, 
                product = product,
                quantity = quantity
                )
            
        return cart_item
    
class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']
    
    def validate_quantity(self, value):
        product = self.instance.product

        if value >= 0:
            if value > product.stock:
                raise serializers.ValidationError(f"Only {product.stock} items remaining in stock.")
            
            return value
            
        raise serializers.ValidationError("Invalid quantity")
    
    

    
    
    
        
        
        
            
            
            
            
    
        