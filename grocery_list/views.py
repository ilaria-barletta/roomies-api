from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GroceryList
from .serializers import GroceryListSerializer
from roomies_api.permissions import IsCreatorOrReadOnly
from django.http import Http404
from rest_framework import status


class GroceryListList(APIView):
    def get(self, request):
        lists = GroceryList.objects.all()

        # From django rest documentation
        # https://www.django-rest-framework.org/api-guide/filtering/
        household_id = self.request.query_params.get("household")

        if household_id is not None:
            lists = GroceryList.objects.filter(household__pk=household_id)
        else:
            lists = GroceryList.objects.filter(creator=self.request.user)

        serializer = GroceryListSerializer(lists, many=True)
        return Response(serializer.data)
