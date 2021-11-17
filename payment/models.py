from django.db import models
from users.models import UserExtended
from training.utilis import current_milli_time
from payment.utilis import random_string


class Transaction(models.Model):
    transaction_id = models.CharField(unique=True, default=random_string, max_length=50)
    user = models.ForeignKey(UserExtended, on_delete=models.CASCADE)
    time = models.IntegerField(default=current_milli_time)
    payed = models.DecimalField(decimal_places=2, max_digits=10)
    purchased = models.IntegerField()


class Offer(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    coins = models.IntegerField()