from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow administrators to edit it.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the admin user.
        return request.user and request.user.is_staff

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

class CanManageCompany(permissions.BasePermission):
    """
    Custom permission to only allow users with the right role to manage company details.
    """

    def has_permission(self, request, view):
        # Permission is only granted to users with the 'can_manage_company' role.
        return request.user and request.user.has_role('can_manage_company')

class CanPublishModule(permissions.BasePermission):
    """
    Custom permission to only allow users with the right role to publish modules.
    """

    def has_permission(self, request, view):
        # Permission is only granted to users with the 'can_publish_module' role.
        return request.user and request.user.has_role('can_publish_module')