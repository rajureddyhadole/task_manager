from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Task
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):

  title = request.data.get('title')
  description = request.data.get('description')
  status = request.data.get('status')

  task = Task.objects.create(
    user=request.user,
    title=title,
    description=description,
    status=status
  )

  if task is not None:
    return Response({
      'message': 'task created successfully',
      'task': {
        'title': task.title,
        'description': task.description,
        'status': task.status,
        'user': task.user.id
      }
    })
  
  return Response({
    'error': 'error occured while creating task'
  })


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_task(request, task_id):
  
  task = get_object_or_404(Task, id=task_id)

  if task.user != request.user:
    return Response({
      'error': 'Not authenticated to make changes to the task'
    }, status=status.HTTP_403_FORBIDDEN)
  
  task.title = request.data.get('title')
  task.description = request.data.get('description')
  task.status = request.data.get('status')

  task.save()

  return Response({
    'message': 'Task updated successfully',
    'task': {
      'title': task.title,
      'description': task.description,
      'status': task.status
    }
  })
