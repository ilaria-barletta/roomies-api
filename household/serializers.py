from rest_framework import serializers
from .models import Household, HouseholdMember


class HouseholdMemberSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = HouseholdMember
        fields = [
            "id",
            "user",
        ]


class HouseholdSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    members = HouseholdMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Household
        fields = ["id", "creator", "rent", "rent_due_day", "name", "members"]
