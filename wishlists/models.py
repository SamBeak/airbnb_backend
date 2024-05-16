from django.db import models
from common.models import CommonModel

class Wishlist(CommonModel):
    
    """ WISHLIST MODEL DEFINITION """
    
    name = models.CharField(
        max_length = 150,
    )
    room = models.ManyToManyField(
        "rooms.Room",
        related_name = "wishlists",
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        related_name = "wishlists",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete = models.CASCADE,
        related_name = "wishlists",
    )
    
    def __str__(self) -> str:
        return self.name