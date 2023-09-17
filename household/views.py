from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Household
from .serializers import HouseholdSerializer


class HouseholdList(APIView):
    def get(self, request):
        households = Household.objects.all()
        serializer = HouseholdSerializer(households, many=True)
        return Response(serializer.data)
