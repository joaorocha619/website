from django.db import models

from artists.models import Artist

class Artwork(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    creation_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='artwork_images/')

    def __str__(self):
        return f'"{self.title}", by {self.artist.name}.'
    
    @classmethod
    def get_recent_artworks(cls, count=10):
        return cls.objects.order_by('-creation_date')[:count]