# from django.shortcuts import render, get_object_or_404
# from . models import Product
# from category.models import Category

# def store(request, category_slug = None):
#     categories = None
#     products = None
    
#     if category_slug != None:
#         categories = get_object_or_404(Category, slug = category_slug)
#         products = Product.objects.filter(category = categories, is_available = True)
#         product_count = products.count()
#     else:
#         products = Product.objects.all().filter(is_available = True)
#         product_count = products.count()
    
#     context = {
#         'products' : products,
#         'product_count' : product_count,
#     }
#     return render(request, 'store/store.html', context)


# def product_detail(request, category_slug, product_slug):
#     try:
#         single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
#     except Exception as e:
#         raise e
#     context = {
        
#         'single_product' : single_product,
#     }
#     return render(request, 'store/product_detail.html', context)
    

from rest_framework import viewsets, filters
from . serializers import ProductSerializer
from . models import Product
from django_filters.rest_framework import DjangoFilterBackend
from . pagination import ProductPagination
from .lru_cache import lru_cache
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



# class ProductViewset(viewsets.ModelViewSet):
    
#     serializer_class = ProductSerializer
#     queryset = Product.objects.select_related('category')
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ['product_name']
#     filterset_fields = {
#     'category': ['exact'],
#     'price': ['exact', 'gte', 'lte']
# }
#     pagination_class = ProductPagination
#     ordering_fields = ['product_name', 'price']
#     ordering = ['id'] #default ordering
    
#     from .lru_cache import lru_cache
# from rest_framework.response import Response

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
        # Cache key based on query params
        cache_key = str(request.query_params)

        # Check cache
        cached_data = lru_cache.get(cache_key)
        if cached_data:
            print("CACHE HIT 🔥")
            return Response(cached_data)

        print("CACHE MISS ❌")

        # Normal queryset flow
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = self.get_paginated_response(serializer.data).data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

        # Store in cache
        lru_cache.put(cache_key, data)

        return Response(data)
    
    