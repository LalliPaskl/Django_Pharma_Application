from django.db import models


# Create your models here.
class Items (models.Model):
    name = models.CharField(max_length=200)
    sheet = models.IntegerField()
    amount = models.FloatField()


class Customers (models.Model):
    customer_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    is_active = models.BooleanField('active', default=False)
