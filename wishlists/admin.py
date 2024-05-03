from django.contrib import admin
from .models import Wishlist

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    
    """ WISHLIST ADMIN CLASS """
    
    list_display = (
        "name",
        "user",
        "created_at",
        "updated_at",
    )
