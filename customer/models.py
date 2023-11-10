from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class CardInfo(models.Model):
    cardholder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.IntegerField()
        

    


class Feedback(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=254, unique=True)
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=500)


class PizzaInfo(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

class Ordersummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()