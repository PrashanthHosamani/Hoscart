from rest_framework.generics import CreateAPIView
from . serializers import Register, Login, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response


class Register(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = Register
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        
        user = serializer.save()
        
        #generate tokens here
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        
        return Response({
            'user' : UserSerializer(user).data,
            'refresh_token' : str(refresh),
            'access_token' : str(access),
        }, status = status.HTTP_201_CREATED)

