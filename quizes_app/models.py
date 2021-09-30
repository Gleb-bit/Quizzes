from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    '''Model for questions'''
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    start_date = models.DateField()
    end_date = models.DateField()
    questions = models.ManyToManyField('Question')

    def __str__(self):
        return self.title


class Question(models.Model):
    CHOICES = [
        ('текст', 'ответ текстом'),
        ('один вариант', 'ответ с выбором одного варианта'),
        ('несколько вариантов', 'ответ с выбором нескольких вариантов'),
    ]

    text = models.TextField(default='')
    type = models.CharField(max_length=255, choices=CHOICES, default='текст')

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4096)
    choice = models.ManyToManyField('Choice', blank=True)

    def __str__(self):
        return self.title


class Choice(models.Model):
    text = models.CharField(max_length=4096, default='')

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Answer, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice.title
