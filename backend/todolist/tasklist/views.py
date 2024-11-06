from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import TodoList, Task
from .serializers import TodoListSerializer, TaskSerializer


class TodoListListCreateView(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    
    def get_queryset(self):
     creator = self.request.user
     if not creator.is_authenticated:
            return TodoList.objects.none()
     return TodoList.objects.filter(creator=creator)



class TodoListDetailView(generics.RetrieveAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodoList.objects.filter(creator=self.request.user)


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Task.objects.none()
        return Task.objects.filter(todolist__creator=user)
    
    def get_serializer_context(self):
        return {'request': self.request}



class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(todolist__creator=self.request.user)
 

class TodoListUpdateView(generics.UpdateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]

  



class TodoListDeleteView(generics.DestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodoList.objects.filter(creator=self.request.user)
    

class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


    
    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Task.objects.none()
        return Task.objects.filter(todolist__creator=user)



class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
     user = self.request.user
     if not user.is_authenticated:
         return Task.objects.none()
     return Task.objects.filter(todolist__creator=user)

