from django.db import models
from common.models import CommonModel

class ChattingRoom(CommonModel):
    
    """ CHATTING ROOM MODEL DEFINITION """
    
    users = models.ManyToManyField(
        "users.User",
        related_name="chatting_rooms",
    )
    
    def __str__(self) -> str:
        return "Chatting Room"
    
class Message(CommonModel):
    
    """ MESSAGE MODEL DEFINITION """
    
    message = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="messages",
    )
    room = models.ForeignKey(
        "ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )
    
    def __str__(self) -> str:
        return f"{self.user} says: {self.message}"