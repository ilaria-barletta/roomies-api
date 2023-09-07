from django.db import models
from django.contrib.auth.models import User


class Household(models.Model):
    name = models.CharField(max_length=255)
    rent = models.IntegerField()
    rent_due_date = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
