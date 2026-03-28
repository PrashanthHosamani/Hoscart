from rest_framework import serializers
from .models import Account
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        
class Register(serializers.ModelSerializer):
    password = serializers.CharField(required = True, write_only = True)
    class Meta:
        model = Account
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email']
        
    def create(self, validated_data):
        user = Account.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            password = validated_data['password'],
            )
        
        return user
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'