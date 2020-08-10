import uuid
from django.db import models
from django.utils import timezone


# Create your models here.

class DefaultDate(models.Model):
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class Topping(DefaultDate):
    topping_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Pizza(DefaultDate):
    pizza_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    toppings = models.ManyToManyField(Topping)
    price = models.DecimalField(max_digits=5, decimal_places=2)

