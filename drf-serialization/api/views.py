from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from .models import Task
from .serializers import TaskSerializer
# Import the user model
from django.contrib.auth.models import User

class TaskView(APIView):
    def get(self, request: Request) -> Response:
        '''get all tasks'''
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        data = serializer.data
        return Response(data)
    
    def post(self, request: Request) -> Response:
        '''add task'''
        data = request.data
        serialzer = TaskSerializer(data=data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        
        return Response(serialzer.errors)
    
    def put(self, request: Request, pk: int) -> Response:
        '''uodate task'''
        try:
            task = Task.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response({'error': 'does not exist'})
        
        data = request.data
        serializer = TaskSerializer(task, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
# Get all users
class UserView(APIView):
    def get(self, request: Request,user:str) -> Response:
        '''Get all user's tasks'''
        try:
            student = User.objects.get(username=user)
        except:
            return Response({'status': 'user required'})
        todos = Task.objects.filter(student=student)
        serializer = TaskSerializer(todos, many=True)
        return Response({
            'first_name': student.first_name,
            'last_name': student.last_name,
            'tasks': serializer.data,
            })   