from rest_framework import permissions


class IsAdminPermission(permissions.BasePermission):
    pass


class IsAdminOrReadOnlyPermission(permissions.BasePermission):
    pass


class IsAuthorPermission(permissions.BasePermission):
    pass


class IsModerator(permissions.BasePermission):
    pass

