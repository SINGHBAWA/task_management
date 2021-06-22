from rest_framework import permissions

class UserTaskPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Client') and view.action in ['list', 'create', 'retrieve']:
            return True
        if request.user and request.user.groups.filter(name='Employee') and view.action in ['list', 'complete_task']:
            return True
        if request.user and request.user.groups.filter(name='Manager') and view.action in ['destroy', 'partial_update', 'update', 'assign_user']:
            return True
        return False