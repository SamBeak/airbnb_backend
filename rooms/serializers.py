from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Room, Amenity
from medias.serializers import PhotoSerializer

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