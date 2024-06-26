from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Room, Amenity
from wishlists.models import Wishilist
from medias.serializers import PhotoSerializer
from categories.serializers import CategorySerializer

class AmenitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Amenity
        fields = (
            "pk",
            "name",
            "description",
        )

class RoomDetailSerializer(serializers.ModelSerializer):
    
    owner = TinyUserSerializer()
    amenities = AmenitySerializer(
        many = True,
        read_only = True,
    )
    category = CategorySerializer(
        read_only = True
    )
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many = True,
        read_only = True,
    )
    
    class Meta:
        model = Room
        fields = "__all__"
    
    def get_rating(self, room):
        return room.rating()
    
    def get_is_owner(self, room):
        request = self.context["request"]
        if request:
            return room.owner == request.user
        return False
    
    def get_is_liked(self, room):
        request = self.context["request"]
        if request:
            if request.user.is_authenticated:
                return Wishilist.objects.filter(
                    user = request.user,
                    rooms_pk = room.pk,
                ).exists()
        return False

class RoomListSerializer(serializers.ModelSerializer):
    
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many = True, 
        read_only = True
    )
    
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
            "photos",
        )
    
    def get_rating(self, room):
        return room.rating()
    
    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user