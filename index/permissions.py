from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOwnerOrReadOnly(BasePermission):
    message = 'شما به این ویو دسترسی ندارید.'

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_superuser or request.user == obj.created_by


class IsSuperUser(BasePermission):
    message = 'شما به این ویو دسترسی ندارید.'

    def has_permission(self, request, view):
        return request.user.is_superuser
