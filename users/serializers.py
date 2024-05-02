from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class TinyUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            "name",
            "avatar",
            "username",
        )

class PrivateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "id",
            "groups",
            "user_permissions",
        )
        
class PublicUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "is_host",
            "name",
            "avatar",
            "gender",
            "language",
            "currency",
        )
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        token["username"]= user.username
        token["name"] = user.name
        return token