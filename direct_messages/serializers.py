from rest_framework.serializers import ModelSerializer
from .models import ChattingRoom, Message

class ChattingRoomSerializer(ModelSerializer):
    
    class Meta:
        model = ChattingRoom
        fields = "__all__"
        
class MessageSerializer(ModelSerializer):
    
    class Meta:
        model = Message
        fields = "__all__"
        