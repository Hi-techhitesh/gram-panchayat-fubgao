from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission to allow admins to write, but others can only read.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for authenticated admin users
        return request.user and request.user.is_authenticated and request.user.is_staff

class IsAdmin(permissions.BasePermission):
    """
    Permission to only allow admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff
