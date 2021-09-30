from rest_framework import serializers
from .models import UserAnswer, Question, Answer, Quiz, Choice


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'start_date', 'end_date', 'description', ]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['pk', 'text', 'type']


class AnswerSerializer(serializers.ModelSerializer):
    choice = serializers.HyperlinkedRelatedField(many=True, queryset=Choice.objects.all(), view_name='choices-detail')

    class Meta:
        model = Answer
        fields = ['pk', 'question', 'choice']


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', ]
