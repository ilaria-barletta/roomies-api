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
    items = GroceryItemSerializer(many=True)

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        list = GroceryList.objects.create(**validated_data)

        # Found here:
        # https://stackoverflow.com/questions/30203652/how-to-get-request-user-in-django-rest-framework-serializer
        user = self.context["request"].user

        for item_data in items_data:
            GroceryItem.objects.create(list=list, creator=user, **item_data)
        return list

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.is_complete = validated_data.get("is_complete", instance.is_complete)
        instance.save()

        # Replace the items with the updated list
        instance.items.all().delete()

        items_data = validated_data.get("items")

        user = self.context["request"].user

        for item_data in items_data:
            GroceryItem.objects.create(list=instance, creator=user, **item_data)

        return instance

    class Meta:
        model = GroceryList
        fields = ["id", "creator", "household", "name", "is_complete", "items"]
