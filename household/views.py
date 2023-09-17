from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Household, HouseholdMember
from .serializers import HouseholdSerializer, HouseholdMemberSerializer
from roomies_api.permissions import IsCreatorOrReadOnly
from django.http import Http404
from rest_framework import status


class HouseholdList(APIView):
    def get(self, request):
        households = Household.objects.all()
        serializer = HouseholdSerializer(households, many=True)
        return Response(serializer.data)


class HouseholdDetail(APIView):
    serializer_class = HouseholdSerializer
    permission_classes = [IsCreatorOrReadOnly]

    def get_object(self, pk):
        try:
            profile = Household.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
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
