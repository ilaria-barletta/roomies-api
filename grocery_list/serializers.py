from rest_framework import serializers
from .models import GroceryList, GroceryItem


class GroceryItemSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = GroceryItem
        fields = [
            "id",
            "creator",
            "name",
            "is_complete",
        ]


class GroceryListSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    # DJ Rest documentation
    # https://www.django-rest-framework.org/api-guide/relations/#example
    items = GroceryItemSerializer(many=True, read_only=True)

    class Meta:
        model = GroceryList
        fields = ["id", "creator", "household", "name", "is_complete", "items"]
