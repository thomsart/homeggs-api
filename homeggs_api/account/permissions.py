from rest_framework import permissions


class IsSuperuser(permissions.BasePermission):
    """
    App: account.\n
    Model: User.\n
    Permission: check if the user is a superuser.\n
    """

    def has_permission(self, request, view):
        return request.user.is_superuser


class IsStaff(permissions.BasePermission):
    """
    App: account.\n
    Model: User.\n
    Permission: check if the user belong to the Admin team.\n
    """

    def has_permission(self, request, view):
        return request.user.is_staff


class IsActive(permissions.BasePermission):
    """
    App: account.\n
    Model: User.\n
    Permission: check if the user is active.\n
    """

    def has_permission(self, request, view):
        return request.user.is_active