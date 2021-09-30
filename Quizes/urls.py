"""Quizes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from quizes_app.api import QuestionViewSet, AnswerViewSet, QuizViewSet, ChoiceViewSet
from quizes_app.views import ChoicesDetail

router = routers.DefaultRouter()
router.register('quizzes', QuizViewSet, 'quizzes')
router.register('questions', QuestionViewSet, 'questions')
router.register('answers', AnswerViewSet, 'answers')
router.register('choices', ChoiceViewSet, 'choices')

schema_view = get_schema_view(
    openapi.Info(
        title='Quiz API',
        default_version='v1',
        description='description of app',
        terms_of_service='https://www.google.com/polices/terms/',
        contact=openapi.Contact(email='admin@company.local'),
        license=openapi.License(name=''),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('<int:pk>/', ChoicesDetail.as_view(), name="choices_detail"),

]