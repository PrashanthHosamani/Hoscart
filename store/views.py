from rest_framework import viewsets, filters
from . serializers import ProductSerializer
from . models import Product
from django_filters.rest_framework import DjangoFilterBackend
from . pagination import ProductPagination
from .lru_cache import lru_cache
from rest_framework.response import Response
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
    

    def list(self, request, *args, **kwargs):
        cache_key = str(request.query_params)

        # Check cache
        cached_data = lru_cache.get(cache_key)
        if cached_data:
            print("CACHE HIT 🔥")
            return Response(cached_data)

        print("CACHE MISS ❌")

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = self.get_paginated_response(serializer.data).data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

        lru_cache.put(cache_key, data)

        return Response(data)
    
    