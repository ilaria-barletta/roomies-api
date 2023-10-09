from rest_framework import serializers
from .models import GroceryList, GroceryItem


class GroceryItemSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    assignee_name = serializers.ReadOnlyField(source="assignee.username")

    class Meta:
        model = GroceryItem
        fields = [
            "id",
            "creator",
            "name",
            "is_complete",
            "assignee",
            "list",
            "assignee_name",
        ]


class GroceryListSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    household_name = serializers.ReadOnlyField(source="household.name")

    class Meta:
        model = GroceryList
        fields = [
            "id",
            "creator",
            "household",
            "name",
            "is_complete",
            "create_date",
            "household_name",
        ]
