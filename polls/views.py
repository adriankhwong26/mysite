from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Question, Choice
from .serializers import ChoiceSerializer, QuestionSerializer

# Create your views here.
@api_view(['POST', 'GET'])
def poll_list(request):
    if request.method == 'GET': # serialization
        queryset = Question.objects.all()
        serializer = QuestionSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST': # deserialization
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Ok')

@api_view(['POST', 'GET'])
def poll_detail(request, id):
    question = get_object_or_404(Question, pk=id)
    serializer = QuestionSerializer(question)

    return Response(serializer.data)

