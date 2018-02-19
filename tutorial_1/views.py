from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        # SERIALIZATION
        # translate model instances into python dictionaries
        # group python dictionaries in python list
        serializer = SnippetSerializer(snippets, many=True)
        # render python list in JSON format
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # DESERIALIZATION
        # parse request into python dictionary
        data = JSONParser().parse(request)
        # translate python dictionary into model instance
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    # get snippet
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == 'GET':
        # SERIALIZATION
        # translate model instances into python dictionary
        serializer = SnippetSerializer(snippet)
        # render python dictionary in JSON format
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        # DESERIALIZATION
        # parse request into python dictionary
        data = JSONParser().parse(request)
        # translate python dictionary into model instance
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
