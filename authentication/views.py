from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    # comment
    # Generated token f743cbd1e215064b6636dde063ff8d2c2aa9aad9 for user mudassir
    def post(self, request ):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        data=request.data
        username=data.get('username','')
        password=data.get('password','')
        user=auth.authenticate(username=username, password=password)

        if user:
            auth_token=jwt.encode({'username':user.username},
                                   settings.JWT_SECRET_KEY,algorithm="HS256")
            serializer=UserSerializer(user)
            data= {
                'user':serializer.data, 'token':auth_token
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'detail':'invalid credential'}, status=status.HTTP_400_BAD_REQUEST)    
          



        #   Generated token 722341aa3f13eed3a31531d236cc492d3a23c792 for user yasir