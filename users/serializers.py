from rest_framework import serializers
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):

  class Meta:
    model = CustomUser
    fields = ['username', 'password', 'email', 'phone', 'age']

    extra_kwargs = {
      'password': {
        'write_only': True
      }
    }

  def create(self, validated_data):
    
    user = CustomUser.objects.create_user(
      username=validated_data['username'],
      password=validated_data['password'],
      email=validated_data['email'],
      phone=validated_data['phone'],
      age=validated_data['age']
    )

    return user
  

class LoginSerializer(serializers.Serializer):

  username = serializers.CharField()

  password = serializers.CharField(
    write_only = True
  )