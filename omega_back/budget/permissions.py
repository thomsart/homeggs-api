from rest_framework import permissions



class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class IsActive(permissions.BasePermission):
    """ This permission just check if the user is active. """

    def has_permission(self, request, view):

        return request.user.is_active