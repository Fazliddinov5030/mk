from rest_framework import permissions

class IsInstructor(permissions.BasePermission):
    """Faqat instructor role li user"""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'instructor')


class IsInstructorOrReadOnly(permissions.BasePermission):
    """Faqat instructorlar yarata oladi, boshqalar o'qiy oladi"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.role == 'instructor')


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Faqat kurs egasi tahrirlaydi, boshqalar faqat o'qiydi"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.instructor == request.user


class IsStudent(permissions.BasePermission):
    """Faqat student role li user"""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'student')