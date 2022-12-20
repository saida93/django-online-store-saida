from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    rate = models.FloatField()
    price = models.FloatField()
    image = models.ImageField()

