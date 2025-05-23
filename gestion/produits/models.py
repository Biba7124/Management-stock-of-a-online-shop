from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image=models.ImageField(null=True,blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0.00)
    countInStock = models.IntegerField(null=False, blank=False, default=0)
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    def has_valid_data(self):
        return bool(self.price and self.countInStock)
