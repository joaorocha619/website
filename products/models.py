from django.db import models
from artworks.models import Artwork

class Product(models.Model):
    name = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    price =models.FloatField()

    def to_csv(self):
        return f"{self.name},{self.price}"