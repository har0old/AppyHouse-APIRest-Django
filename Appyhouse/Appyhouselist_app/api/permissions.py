from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        
        staff_permission= bool(request.user and request.user.is_staff)
        return staff_permission
    
class CommentUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else: 
            return obj.comment_user == request.user