from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.creator == request.user


class CanManageHousehold(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_member = obj.members.all().filter(user=request.user)
        return obj.creator == request.user or is_member


class CanManageGroceryList(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_member = obj.household.members.all().filter(user=request.user)
        return obj.creator == request.user or is_member


class CanManageGroceryItem(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_member = obj.list.household.members.all().filter(user=request.user)
        return obj.creator == request.user or is_member
