from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # print('obj',obj)
        # print('obj.id',obj.id)
        # print('request.user = ',request.user,' ',request.user.id)
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.id
