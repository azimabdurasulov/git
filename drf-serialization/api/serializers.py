from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=10,
        required=True,
        error_messages={
        'required': 'Fist name is required',
        'max_length': 'Fist name is too long',
        })
    # last_name = serializers.CharField(
    #     max_length=60,
    #     required=True,
    #     error_messages={
    #     'required': 'Last name is required',
    #     'max_length': 'Last name is too long',
    #     })
    
    class Meta:
        model = Task
        fields = '__all__'

    # def to_representation(self, instance):
    #     return {
    #         "id": instance.id,
    #         "title": instance.title,
    #     }
