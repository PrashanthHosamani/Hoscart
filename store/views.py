from rest_framework import viewsets, filters
from .serializers import ProductSerializer
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import ProductPagination
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = ProductSerializer
    queryset = Product.objects.select_related('category')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['product_name']
    filterset_fields = {
        'category': ['exact'],
        'price': ['exact', 'gte', 'lte']
    }
    pagination_class = ProductPagination
    ordering_fields = ['product_name', 'price']
    ordering = ['id']