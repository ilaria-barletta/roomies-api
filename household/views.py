from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Household, HouseholdMember
from .serializers import HouseholdSerializer, HouseholdMemberSerializer
from roomies_api.permissions import CanManageHousehold
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework import status


class HouseholdList(generics.ListCreateAPIView):
    serializer_class = HouseholdSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        creator_households = Household.objects.filter(creator=user)

        user_memberships = list(user.memberships.all())
        user_household_ids = list(map(lambda m: m.household.id, user_memberships))
        member_households = Household.objects.filter(pk__in=user_household_ids)

        # Found here
        # https://stackoverflow.com/questions/431628/how-to-combine-multiple-querysets-in-django
        return creator_households | member_households

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class HouseholdDetail(APIView):
    serializer_class = HouseholdSerializer
    permission_classes = [CanManageHousehold]

    def get_object(self, pk):
        try:
            household = Household.objects.get(pk=pk)
            self.check_object_permissions(self.request, household)
            return household
        except Household.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        household = self.get_object(pk)
        serializer = HouseholdSerializer(household, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        household = self.get_object(pk)
        serializer = HouseholdSerializer(
            household, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        household = self.get_object(pk)
        household.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HouseholdMembersList(APIView):
    def get(self, request, pk):
        household = Household.objects.get(pk=pk)
        serializer = HouseholdMemberSerializer(household.members.all(), many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        household = Household.objects.get(pk=pk)
        serializer = HouseholdMemberSerializer(
            data=request.data, context={"request": request}
        )

        user_id = request.data.get("user")
        is_existing_member = household.members.all().filter(user=user_id)

        if is_existing_member:
            return Response(
                "This user is already a member of this household.",
                status=status.HTTP_400_BAD_REQUEST,
            )

        if serializer.is_valid():
            serializer.save(household=household)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HouseholdMembersDetail(APIView):
    def get(self, request, household_pk, pk):
        member = HouseholdMember.objects.get(pk=pk)
        serializer = HouseholdMemberSerializer(member)
        return Response(serializer.data)

    def delete(self, request, household_pk, pk):
        member = HouseholdMember.objects.get(pk=pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
