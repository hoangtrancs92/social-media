from rest_framework import status, authentication, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializer import UserSerializer
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import *

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            # Create or get token for user
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username, 'id': user.id})
        except Exception as e:
            return Response({'error': 'User or password is incorrect!'}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.create_user(**serializer.validated_data)
            return Response({'status': 'success', 'message': 'The user %s register successfully' %(user.username)}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class UserDetailView(generics.RetrieveAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer

#     def get_object(self):
#         return self.request.user
class UserDetailAPIView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        
        # Lấy token từ request header hoặc request body
        token_key = self.request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        # Tìm token tương ứng
        token = Token.objects.get(key=token_key)
        # Trả về user của token
        return token.user
    def get_current_User(self, request):
        user = request.user
        if user.is_authenticated:
            return user
        else:
            # return Response({'error': 'User not authenticated'})
            raise AuthenticationFailed({'error': 'User not authenticated'})



