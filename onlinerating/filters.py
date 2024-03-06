from django.db.models import QuerySet
from rest_framework import filters

from onlinerating.models import AccessRights, Questionnaire


class AccessedQuestionnairesFilter(filters.BaseFilterBackend):  # Фильтрует по пользователю и его правам
    def filter_queryset(self, request, queryset: QuerySet, view):
        accessepted = []
        if not request.user.is_anonymous:
            if request.user.is_superuser:
                return queryset
            rights = AccessRights.objects.filter(user=request.user, can_view_answers=True).values("questionnaire_id")
            return queryset.filter(pk__in=rights)
        else:
            return Questionnaire.objects.none()


class ShowAdminsOnlyForAdminFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(is_superuser=False)
