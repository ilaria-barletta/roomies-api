from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Household(models.Model):
    name = models.CharField(max_length=255)
    rent = models.IntegerField()
    rent_due_day = models.IntegerField(
        validators=[MaxValueValidator(31), MinValueValidator(1)], default=1
    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class HouseholdMember(models.Model):
    user = models.ForeignKey(User, related_name="memberships", on_delete=models.CASCADE)
    household = models.ForeignKey(
        Household, related_name="members", on_delete=models.CASCADE
    )
