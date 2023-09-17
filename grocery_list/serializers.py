from rest_framework import serializers
from .models import GroceryList


class GroceryListSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    household = serializers.ReadOnlyField(source="household.name")

    class Meta:
        model = GroceryList
        fields = [
            "id",
            "creator",
            "household",
            "name",
            "is_complete",
        ]
