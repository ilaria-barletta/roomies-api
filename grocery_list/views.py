from rest_framework import generics
from .models import GroceryList
from .serializers import GroceryListSerializer
from roomies_api.permissions import CanManageGroceryList


class GroceryListList(generics.ListCreateAPIView):
    serializer_class = GroceryListSerializer

    def get_queryset(self):
        queryset = GroceryList.objects.all()

        # From django rest documentation
        # https://www.django-rest-framework.org/api-guide/filtering/
        household_id = self.request.query_params.get("household")

        if household_id is not None:
            queryset = GroceryList.objects.filter(household__pk=household_id)
        else:
            queryset = GroceryList.objects.filter(creator=self.request.user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class GroceryListDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroceryListSerializer
    permission_classes = [CanManageGroceryList]
    queryset = GroceryList.objects.all()
