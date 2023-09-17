from rest_framework import serializers
from .models import Household


class HouseholdSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = Household
        fields = [
            "id",
            "creator",
            "rent",
            "rent_due_date",
            "name",
        ]
