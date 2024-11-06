from rest_framework import serializers
from .models import TodoList, Task


class TaskSerializer(serializers.ModelSerializer):

    todolist = serializers.PrimaryKeyRelatedField(queryset=TodoList.objects.none())
    class Meta:
        model = Task
        fields = ['task_id', 'title', 'description', 'status','todolist']

    def __init__(self, *args, **kwargs):
            super(TaskSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and hasattr(request, 'user'):
                self.fields['todolist'].queryset = TodoList.objects.filter(creator=request.user)

class TodoListSerializer(serializers.ModelSerializer):
    todos = TaskSerializer(many=True, read_only=True)  

    class Meta:
        model = TodoList
        fields = ['id', 'title', 'todos']
      

