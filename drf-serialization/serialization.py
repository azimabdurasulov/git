from rest_framework import serializers


class Task():
    def __init__(self, id, title, description, done):
        self.id          = id
        self.title       = title
        self.description = description
        self.done        = done


class TaskSerializer(serializers.Serializer):
    id          = serializers.IntegerField()
    title       = serializers.CharField()
    description = serializers.CharField()
    done        = serializers.BooleanField()


task = Task(1, 'title', 'nimadir', True)

serializer = TaskSerializer(task)
data = serializer.data
print(data)