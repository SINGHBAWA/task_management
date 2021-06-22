from rest_framework import mixins, response, viewsets
from tasks import serializers
from tasks.models import Task
from tasks.choices import TaskStatus
from tasks.serializers import TaskSerializer, TaskAssignedToSerializer
from rest_framework.decorators import action
from tasks.permissions import UserTaskPermission

class TaskCreateListUpdateView(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               viewsets.GenericViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (UserTaskPermission, )

    @action(detail=True, methods=['put'])
    def complete_task(self, request, pk=None):
        task = self.get_object()
        task.status = TaskStatus.complete
        task.save()
        data= self.serializer_class(instance=task).data 
        return response.Response({'status': 'Task Completed'})
    
    
    @action(detail=True, methods=['put'])
    def assign_user(self, request, pk=None):
        obj = self.get_object()
        serializer = TaskAssignedToSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"data": serializer.data})
        else:
            return response.Response({ "data": serializer.errors}, status=400)
