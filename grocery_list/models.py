from django.db import models
from household.models import Household
from django.contrib.auth.models import User


class GroceryList(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    is_complete = models.BooleanField()

    def __str__(self):
        return self.name


class GroceryItem(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_complete = models.BooleanField()
    list = models.ForeignKey(
        GroceryList, on_delete=models.CASCADE, related_name="items"
    )

    def __str__(self):
        return self.name