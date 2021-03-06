from django.db import models

# Create your models here.
from training.utilis import current_milli_time
from users.models import UserExtended


class Message(models.Model):
    sender = models.ForeignKey(UserExtended, on_delete=models.CASCADE, null=True, default=None, related_name='sender')
    receiver = models.ForeignKey(UserExtended, on_delete=models.CASCADE, null=True, default=None,
                                 related_name='receiver')

    time = models.IntegerField(default=current_milli_time)
    message = models.CharField(max_length=10000)


class Notification(models.Model):
    user = models.ForeignKey(UserExtended, on_delete=models.CASCADE)

    USER_REGISTERED = '0'
    APPLICATION_ACCEPTED = '1'
    APPLICATION_REJECTED = '2'
    TRAINING_GROUP_INIVITATION = '3'
    TRAINING_GROUP_JOIN = '4'
    TRAINING_GROUP_USER_HAS_JOINED = '5'
    DIET_GROUP_JOIN = '6'
    DIET_GROUP_USER_HAS_JOINED = '7'
    GYMCOIN_BOUGHT = '8'
    TYPE_CHOICES = [
        (USER_REGISTERED, 'USER REGISTERED'),
        (APPLICATION_ACCEPTED, 'APPLICATION ACCEPTED'),
        (APPLICATION_REJECTED, 'APPLICATION REJECTED'),
        (TRAINING_GROUP_INIVITATION, 'TRAINING_GROUP_INIVITATION'),
        (TRAINING_GROUP_JOIN, 'TRAINING_GROUP_JOIN'),
        (TRAINING_GROUP_USER_HAS_JOINED, 'TRAINING_GROUP_USER_HAS_JOINED'),
        (DIET_GROUP_JOIN, 'DIET_GROUP_JOIN'),
        (DIET_GROUP_USER_HAS_JOINED, 'DIET_GROUP_USER_HAS_JOINED'),
        (GYMCOIN_BOUGHT, ' GYMCOIN_BOUGHT'),
    ]

    kind = models.CharField(max_length=1, choices=TYPE_CHOICES, default=None)

    body = models.CharField(max_length=10000)
    time = models.IntegerField(default=current_milli_time)
    seen = models.BooleanField(default=False)
