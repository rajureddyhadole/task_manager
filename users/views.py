from django.shortcuts import render
from .models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def register(request):
  username = request.data.get('username')
  password = request.data.get('password')
  email = request.data.get('email')
  phone = request.data.get('phone')
  age = request.data.get('age')

  CustomUser.objects.create_user(
    username=username,
    password=password,
    email=email,
    phone=phone,
    age=age,
  )

  return Response({
    'message': 'You have been registered. Welcome!'
  })


@api_view(['POST'])
def login_view(request):

  username = request.data.get('username')
  password = request.data.get('password')

  user = authenticate(
    username=username,
    password=password,
  )

  if user is not None:
    refresh = RefreshToken.for_user(user)

    return Response({
      'access': str(refresh.access_token),
      'refresh': str(refresh),
      'user': {
        'id': user.id,
        'username': user.username,
        'email': user.email
      }
    })
  
  return Response({'error': 'Invalid credetials'}, status=status.HTTP_401_UNAUTHORIZED)