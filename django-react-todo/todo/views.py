from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import taskSerializer
from .models import *

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    lists = todoList.objects.all()
    serializer = taskSerializer(lists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    lists = todoList.objects.get(id=pk)
    serializer = taskSerializer(lists, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = taskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    lists = todoList.objects.get(id=pk)
    serializer = taskSerializer(instance=lists, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    lists = todoList.objects.get(id=pk)
    lists.delete()
    return Response('Item successfully deleted!')