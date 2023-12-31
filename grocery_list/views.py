from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import GroceryList, GroceryItem, GroceryListComment
from .serializers import (
    GroceryListSerializer,
    GroceryItemSerializer,
    GroceryListCommentSerializer,
)
from roomies_api.permissions import (
    CanManageGroceryList,
    CanManageGroceryItem,
    IsCreatorOrReadOnly,
)


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


class GroceryItemList(generics.ListCreateAPIView):
    serializer_class = GroceryItemSerializer
    queryset = GroceryItem.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    # https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html#using-the-filterset-fields-shortcut
    filterset_fields = ["list", "is_complete", "assignee"]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class GroceryListCommentList(generics.ListCreateAPIView):
    serializer_class = GroceryListCommentSerializer
    queryset = GroceryListComment.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    # https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html#using-the-filterset-fields-shortcut
    filterset_fields = ["list", "creator"]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class GroceryListCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroceryListCommentSerializer
    permission_classes = [IsCreatorOrReadOnly]
    queryset = GroceryListComment.objects.all()


class GroceryItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroceryItemSerializer
    permission_classes = [CanManageGroceryItem]
    queryset = GroceryItem.objects.all()
