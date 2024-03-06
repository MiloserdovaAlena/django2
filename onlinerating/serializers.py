import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers

from onlinerating.models import Questionnaire, EmployeeFeedback, AccessRights

user_model = get_user_model()


class QuestionnaireSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ['title', 'description']

    def validate_title(self, value):
        if Questionnaire.objects.filter(title=value).exists():
            raise serializers.ValidationError('Анкета с таким названием уже существует.')
        return value


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = user_model
        fields = ['id', 'email', 'username', 'is_superuser']


class AccessRightsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = AccessRights
        fields = ['questionnaire', 'can_view_answers', 'user']

    def validate_title(self, value):
        if Questionnaire.objects.filter(title=value).exists():
            raise serializers.ValidationError('Анкета с таким названием уже существует.')
        return value


class EmployeeFeedbackSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeFeedback
        fields = ['anonymous_user', 'feedback', 'rating', 'date_created', 'user']

    def validate_rating(self, value):
        if not (0 <= value <= 5):
            raise serializers.ValidationError("Rating must be gte 0 and lte 5 ")
        return value
