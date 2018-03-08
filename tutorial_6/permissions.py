from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # custom permission to only allow owners of an object to edit it
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
