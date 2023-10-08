from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import GroceryList
from .serializers import GroceryListSerializer
from roomies_api.permissions import CanManageGroceryList


class GroceryListList(generics.ListCreateAPIView):
    serializer_class = GroceryListSerializer
    queryset = GroceryList.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    # https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html#using-the-filterset-fields-shortcut
    filterset_fields = ["household", "is_complete"]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class GroceryListDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroceryListSerializer
    permission_classes = [CanManageGroceryList]
    queryset = GroceryList.objects.all()
