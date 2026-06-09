from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CartItemSerializer, AddToCartSerializer, UpdateCartItemSerializer
from .models import CartItem, Cart
from rest_framework import status
from django.shortcuts import get_object_or_404


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]
        
    def post(self, request):
        serializer = AddToCartSerializer(data = request.data, context = {'request' : request})
        if serializer.is_valid():
            cart_item = serializer.save()
            item_serializer = CartItemSerializer(cart_item)
            return Response(item_serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request):
        Cart_Items = CartItem.objects.filter(cart__user = request.user)
        
        serializer = CartItemSerializer(Cart_Items, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class UpdateCartItem(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request, pk, **args):
        item_object = get_object_or_404(CartItem, pk=pk, cart__user = request.user)
        
        serializer = UpdateCartItemSerializer(item_object, data = request.data, partial = True)
        
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self, request, pk, **args):
        item_object = get_object_or_404(CartItem, pk=pk, cart__user = request.user)
  
        item_object.delete()
        
        return Response(f"{(item_object.product.product_name)} deleted from the cart", status = status.HTTP_200_OK)
        
    
            