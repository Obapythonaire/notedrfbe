from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import *
from .serializers import *
from . utils import *




# We are about to make our API RESTful
# Any difference between the two? API and RESTful API?
# For instance, as it is now, we have multiple routes handling
# different HTTP requests(GET, POST, PUT, DELETE)
# e.g notes/
# notes/create
# notes/delete
# notes/<str:id> etc
# Doing the above makes our API not RESTful
# To make it RESTful, we will have only two end-points and routes that will handle all HTTP request
# i.e /notes  GET
# /notes POST
# /notes/<id> GET
# /notes/<id> PUT
# /notes/<id> DELETE

# isn't that great, let's now make our API RESTful


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    # return JsonResponse('Our API', safe=False)
    return Response('Our API')

@api_view(['GET', 'POST'])
def Notes(request):
    if request.method == 'GET':
        return getAllNotes(request)
        # notes = Note.objects.all()
        # serializer = NoteSerializer(notes, many=True)
        # return Response(serializer.data)
    
    if request.method == 'POST':
        return createNote(request) 
        # data = request.data
        # note = Note.objects.create(
        # body=data['body']
        # )
        # serializer = NoteSerializer(note, many=False)

        # return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):

    if request.method == 'GET':
        return getNoteDetail(request, pk)
        # notes = Note.objects.get(id=pk)
        # serializer = NoteSerializer(notes, many=False)
        # return Response(serializer.data)
    
    # if request.method == 'POST':
        # return createNote(request) 
    #     data = request.data
    #     note = Note.objects.create(
    #     body=data['body']
    #     )
    #     serializer = NoteSerializer(note, many=False)

    #     return Response(serializer.data)
    
    if request.method == 'PUT':
        return updateNote(request, pk)
    #     data = request.data
    #     note = Note.objects.get(id=pk)
    #     serializer = NoteSerializer(instance=note, data=data)

    #     if serializer.is_valid():
    #         serializer.save()

    #     return Response(serializer.data)
    
    if request.method == 'DELETE':
        return deleteNote(request, pk)
    #     note = Note.objects.get(id=pk)
    #     note.delete()

    #     return Response('Note Successfully Deleted!')

# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body=data['body']
#     )
#     serializer = NoteSerializer(note, many=False)

#     return Response(serializer.data)

# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['DELETE'])
# def DeleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()

#     return Response('Note Successfully Deleted!')