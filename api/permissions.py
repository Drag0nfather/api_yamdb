from rest_framework import permissions


class IsAdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_admin


class IsAdminOrReadOnlyPermission(permissions.BasePermission):
    pass


class IsAuthorPermission(permissions.BasePermission):
    pass


class IsModerator(permissions.BasePermission):
    pass

