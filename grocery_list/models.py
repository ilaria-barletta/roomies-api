from django.db import models
from household.models import Household
from django.contrib.auth.models import User


class GroceryList(models.Model):
    name = models.CharField(max_length=255)
    create_date = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    is_complete = models.BooleanField()

    def __str__(self):
        return self.name


class GroceryListComment(models.Model):
    content = models.CharField(max_length=255)
    create_date = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey(
        GroceryList, on_delete=models.CASCADE, related_name="comments"
    )

    def __str__(self):
        return self.content


class GroceryItem(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="assigned_grocery_items",
    )
    is_complete = models.BooleanField()
    list = models.ForeignKey(
        GroceryList, on_delete=models.CASCADE, related_name="items"
    )

    def __str__(self):
        return self.name
