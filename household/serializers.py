from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Household, HouseholdMember


class HouseholdMemberSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = HouseholdMember
        fields = ["id", "user", "user_name"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class HouseholdSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    members = HouseholdMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Household
        fields = ["id", "creator", "rent", "rent_due_day", "name", "members"]
