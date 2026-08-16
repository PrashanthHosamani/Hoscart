import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from order.models import Order
from .models import Payment
from .serializers import StripeCheckoutSerializer, StripeVerifySerializer

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeCheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = StripeCheckoutSerializer(data=request.data)
        if serializer.is_valid():
            order_id = serializer.validated_data['order_id']
            
            try:
                order = Order.objects.get(id=order_id, user=request.user, status="PENDING")
                
                payment, created = Payment.objects.get_or_create(
                    order=order,
                    defaults={'amount': order.total_amount, 'status': 'PENDING'}
                )
                
                intent = stripe.PaymentIntent.create(
                    amount=int(order.total_amount * 100),
                    currency='usd', 
                    metadata={'order_id': order.id}
                )
                
                payment.stripe_payment_id = intent['id']
                payment.save()
                
                return Response({'clientSecret': intent['client_secret']}, status=status.HTTP_200_OK)
                
            except Order.DoesNotExist:
                return Response({"error": "Order not found or already paid."}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StripeVerifyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = StripeVerifySerializer(data=request.data)
        if serializer.is_valid():
            payment_intent_id = serializer.validated_data['payment_intent_id']
            
            try:
                intent = stripe.PaymentIntent.retrieve(payment_intent_id)
                
                if intent.status == 'succeeded':
                    payment = Payment.objects.get(stripe_payment_id=payment_intent_id)
                    payment.status = "COMPLETED"
                    payment.save()
                    
                    order = payment.order
                    order.status = "PAID"
                    order.save()
                    
                    return Response({"message": "Payment Successful", "order_id": order.id}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Payment not successful"}, status=status.HTTP_400_BAD_REQUEST)
                    
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
