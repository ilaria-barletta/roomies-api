from django.contrib import admin
from .models import GroceryList, GroceryItem

admin.site.register([GroceryList, GroceryItem])
