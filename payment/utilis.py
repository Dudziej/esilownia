from django.utils.crypto import get_random_string
from payment import models
from django.db import transaction


# code = get_random_string(5)


def random_string():
    return get_random_string(16)


@transaction.atomic
def create_transaction(user, offer_id):
    offer = models.Offer.objects.get(id=offer_id)
    transaction = models.Transaction.objects.create(user=user, payed=offer.price, purchased=offer.coins)
    user.money += offer.coins
    user.save()
    transaction.save()
    return transaction