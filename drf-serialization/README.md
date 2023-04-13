# drf-serialization

this is a simple example of how to use drf-serialization. Todo list project without authentication.

## Installation

```bash
pip install -r requirements.txt
```

## Serialization object to json

- Task object

```python
class Task():
    def __init__(self, id, title, description, done):
        self.id          = id
        self.title       = title
        self.description = description
        self.done        = done
```

- TaskSerializer

```python
from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    id          = serializers.IntegerField()
    title       = serializers.CharField()
    description = serializers.CharField()
    done        = serializers.BooleanField()

    def create(self, validated_data):
        task = Task(id=validated_data['id'],
                    title=validated_data['title'],
                    description=validated_data['description'],
                    done=validated_data['done'])
        return task
```

- TaskSerializer to json

```python
task = Task(1, 'title', 'description', False)
serializer = TaskSerializer(task)
data = serializer.data
print(data)
```

## Deserialization json to object

```python
data = {
    'id': 1,
    'title': 'title',
    'description': 'description',
    'done': False
}

serializer = TaskSerializer(data=data)
if serializer.is_valid():
    task = serializer.save()
    print(task.title)
```
