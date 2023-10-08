from rest_framework import serializers
from .models import GroceryList, GroceryItem


class GroceryItemSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = GroceryItem
        fields = ["id", "creator", "name", "is_complete", "assignee", "list"]


class GroceryListSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = GroceryList
        fields = ["id", "creator", "household", "name", "is_complete", "create_date"]
