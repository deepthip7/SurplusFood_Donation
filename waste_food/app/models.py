from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    temperature = models.CharField(max_length=20)
    restaurant_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    assigned = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.restaurant_name})"