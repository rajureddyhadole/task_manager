from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Task
from rest_framework.response import Response

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
