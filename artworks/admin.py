from django.contrib import admin
from .models import Artwork, Artist

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'creation_date')
    list_filter = ('artist', 'creation_date')
    search_fields = ('title', 'description')

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    list_filter = ('name', 'bio')
    search_fields = ('name', 'bio')