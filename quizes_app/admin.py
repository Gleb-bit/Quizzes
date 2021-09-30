from django.contrib import admin
from .models import Question, UserAnswer, Answer, Quiz, Choice


class QuizAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'start_date',
        'end_date',
    )


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'type',
    )


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'question',
    )
    list_filter = ('question',)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'text',
    )


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'choice',
    )
    list_filter = ('user',)


admin.site.register(Quiz, QuizAdmin)

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice, ChoiceAdmin)

admin.site.register(Answer, AnswerAdmin)

admin.site.register(UserAnswer, UserAnswerAdmin)
