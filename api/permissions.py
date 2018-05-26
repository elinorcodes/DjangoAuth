from rest_framework import permissions

class UserGroupPermissions(permissions.BasePermission):
    
    message = 'Write methods aren\'t allowed to you!'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff or request.user.profile.group=='A'
