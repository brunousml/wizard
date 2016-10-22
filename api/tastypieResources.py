from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import Choice, Question


class QuestionResource(ModelResource):
    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'
        always_return_data = True
        authorization = Authorization()


class ChoiceResource(ModelResource):
    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choice'