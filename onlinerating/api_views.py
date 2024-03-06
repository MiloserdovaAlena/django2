from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

from onlinerating.filters import AccessedQuestionnairesFilter, ShowAdminsOnlyForAdminFilter
from onlinerating.models import Questionnaire, EmployeeFeedback
from onlinerating.serializers import QuestionnaireSerializer, EmployeeFeedbackSerializer, UserSerializer
from .pagination import CustomPagination

user_model = get_user_model()


class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    pagination_class = CustomPagination

    filter_backends = [AccessedQuestionnairesFilter, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['title', 'description']
    ordering_fields = ['title']
    search_fields = ['title', 'description']


class UserViewSet(viewsets.ModelViewSet):  # /api/user/filter_users/?email=admin&username=admin
    queryset = user_model.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    
    filter_backends = [ShowAdminsOnlyForAdminFilter, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'email']
    ordering_fields = ['username', 'email', 'is_superuser']

    @action(detail=False, methods=['get'])
    def filter_users(self, request):
        email = self.request.query_params.get('email')
        username = self.request.query_params.get('username')
        if email is not None and username is not None:
            queryset = self.get_queryset().filter(
                Q(is_superuser=False) & (Q(username__startswith=username) | Q(email__startswith=email))
            )
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        else:
            return self.list(request)


class EmployeeFeedbackViewSet(viewsets.ModelViewSet):
    queryset = EmployeeFeedback.objects.all()
    serializer_class = EmployeeFeedbackSerializer
    pagination_class = CustomPagination

    @action(detail=False, methods=['get'])
    def filter_feedback(self, request):
        created = self.request.query_params.get('created')
        rating_gt = self.request.query_params.get('rating_gt')
        rating_lt = self.request.query_params.get('rating_lt')
        if created is not None and rating_gt is not None and rating_lt is not None:

            queryset = self.get_queryset().filter(
                Q(date_created=created) & Q(rating__gt=rating_gt) | Q(rating__lt=rating_lt)
            )
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return self.list(request)

    @action(detail=True, methods=['post'])
    def add_employee_feedback(self, request):
        serializer = EmployeeFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
