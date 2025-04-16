"""
Module for account views
"""

from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserSerializer, CreateUserSerializer, UpdateUserSerializer, LoginUserSerializer


class UserLogin(APIView):

    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):

        data = request.data
        # assert validate_email(data)
        # assert validate_password(data)
        serializer = LoginUserSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            serializer = UserSerializer(user)
            login(request, user)

            return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):

    def post(self, request):

        logout(request)

        return Response(status=status.HTTP_200_OK)