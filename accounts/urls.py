from django.urls import path, include
from . views import Register, MyTokenObtainPairLogin

urlpatterns = [
    path('register/', Register.as_view(), name = 'register'),
    path('login/', MyTokenObtainPairLogin.as_view(), name = 'login')
]
