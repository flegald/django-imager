"""Permissions for API."""
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Allow only objects the logged in user is the owner of to show."""

    def owner_permission(self, request, view, obj):
        """Get objects user owns."""
        return all([obj.owner == request.user,
                    request.method in permissions.SAFE_METHODS])
