from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        # SERIALIZATION
        # translate model instances into python dictionaries
        # group python dictionaries in python list
        serializer = SnippetSerializer(snippets, many=True)
        # render python list in JSON format
        return Response(serializer.data)

    elif request.method == 'POST':
        # DESERIALIZATION
        # parse request into python dictionary
        # translate python dictionary into model instance
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    # get snippet
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        # SERIALIZATION
        # translate model instances into python dictionary
        serializer = SnippetSerializer(snippet)
        # render python dictionary in JSON format
        return Response(serializer.data)

    elif request.method == 'PUT':
        # DESERIALIZATION
        # parse request into python dictionary
        # translate python dictionary into model instance
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
