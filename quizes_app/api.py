from datetime import datetime

from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from .serializers import QuestionSerializer, AnswerSerializer, QuizSerializer, ChoiceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from .models import Question, Quiz, Choice, Answer


class QuizViewSet(viewsets.ModelViewSet):
    '''Information about quizzes'''

    queryset = Quiz.objects.filter(start_date__lte=datetime.now(), end_date__gte=datetime.now())
    serializer_class = QuizSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    '''Information about choices of questions'''

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    '''Information about question'''

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class AnswerViewSet(viewsets.ModelViewSet):
    '''Page for answering on questions'''

    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

