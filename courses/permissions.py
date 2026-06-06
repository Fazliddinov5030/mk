from rest_framework import permissions

class IsInstructor(permissions.BasePermission):
    """Faqat instructor role li user"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'instructor'


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Faqat kurs egasi tahrirlaydi, boshqalar faqat o'qiydi"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.instructor == request.user