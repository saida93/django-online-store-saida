from django.db import models

class Category(models.Model):
    title =models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    rate = models.FloatField()
    price = models.FloatField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True)
    created_date = models.DateField(auto_now= True)

    def __str__(self):
        return self.text

