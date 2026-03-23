from django.urls import path, include 
from . import views
from rest_framework.routers import DefaultRouter
from . views import ProductViewset

router = DefaultRouter()
router.register(r'product', ProductViewset, basename='product')
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls))
]
