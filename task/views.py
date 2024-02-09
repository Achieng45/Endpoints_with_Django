from http.client import responses
import json
from urllib import response
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return HttpResponse(serializer.data)
    
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
        return HttpResponse(f"data is saved")

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@csrf_exempt
def update_task_status(request, task_id):
    if request.method == 'POST':
        try:
            # Parse the JSON request body
            data = json.loads(request.body.decode('utf-8'))
            new_status = data.get('status')

            task = Task.objects.get(pk=task_id)
            task.status = new_status
            task.save()
            return JsonResponse({'message': 'Task status updated successfully.'}, status=200)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    
def get_tasks_by_status(request, status):
    if request.method == 'GET':
        try:
            tasks = Task.objects.filter(status=status)
            serialized_tasks = [{'id': task.id, 'name': task.name, 'description': task.description, 'status': task.status} for task in tasks]
            return JsonResponse({'tasks': serialized_tasks}, status=200)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Tasks not found for the given status.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    
@csrf_exempt   
def delete_all_tasks(request):
    if request.method == 'DELETE':
        try:
            # Delete all tasks from the database
            Task.objects.all().delete()
            return JsonResponse({'message': 'All tasks deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': 'Failed to delete tasks.', 'details': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    
@api_view(['DELETE'])
def delete_task_by_id(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': f'Task with ID {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        task.delete()
        return Response({'message': f'Task with ID {pk} deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)