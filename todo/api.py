from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer
from .pagination import CustomPagination


class TodoViewSet(viewsets.ModelViewSet):
    pagination_class = CustomPagination
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.all()
        completed = self.request.query_params.get('completed')
        in_completed = self.request.query_params.get('in_completed')
        if completed is not None:
            queryset = queryset.filter(done=True)
        if in_completed is not None:
            queryset = queryset.filter(done=False)
        return queryset.order_by('-date_update')
