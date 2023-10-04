from django.db import models
from artworks.models import Artwork

class Order(models.Model):
    # Fields: product, quantity, price, ...
    product = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    def calculate_total(self):
        return self.quantity * self.price