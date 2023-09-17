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
