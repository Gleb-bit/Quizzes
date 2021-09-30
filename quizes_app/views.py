from django.views import generic

from quizes_app.models import Choice


class ChoicesDetail(generic.DetailView):
    model = Choice
