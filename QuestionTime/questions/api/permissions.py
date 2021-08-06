from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Override has_obj method to provide write permission to auth users only"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
