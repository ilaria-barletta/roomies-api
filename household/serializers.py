from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Household, HouseholdMember


class HouseholdMemberSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = HouseholdMember
        fields = ["id", "user", "user_name", "has_paid_rent"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class HouseholdSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    creator_id = serializers.ReadOnlyField(source="creator.id")
    members = HouseholdMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Household
        fields = [
            "id",
            "creator",
            "rent",
            "rent_due_day",
            "name",
            "members",
            "creator_id",
        ]
