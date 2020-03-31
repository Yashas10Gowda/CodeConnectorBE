from rest_framework import permissions

class DeveloperPermission(permissions.BasePermission):
    def has_object_permission(self,request,_,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.user.id
    
    
class EEPermission(permissions.BasePermission):
    def has_object_permission(self,request,_,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.whose.user.id
    
    
class UserPermission(permissions.BasePermission):
    def has_object_permission(self,request,_,obj):
        return request.user.id == obj.id