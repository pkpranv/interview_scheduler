from rest_framework import permissions


class IsHRUser(permissions.BasePermission):
    "Allow the requests which has role as HR"

    def has_permission(self, request, view):
        if request.user.role == 'HR':
            return True
        return False

class IsNonHRUser(permissions.BasePermission):
    "Allow the requests which has role as HR"

    def has_permission(self, request, view):
        if request.user.role != 'HR':
            return True
        return False
    
