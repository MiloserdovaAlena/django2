import datetime

from django.contrib import admin
from import_export.admin import ExportMixin, ImportExportModelAdmin

from .models import Questionnaire, Answer, AccessRights, EmployeeFeedback, ManagerFeedback, SelfFeedback, \
    ColleagueFeedback
from .resources import EmployeeFeedbackResource


# Кастомный метод для отображения средней оценки в списке ответов о сотруднике
def average_rating(obj):
    return obj.calculate_average_rating()


average_rating.short_description = 'Средний рейтинг'


class EmployeeFeedbackAdmin(ImportExportModelAdmin):
    list_display = ('user', 'feedback', 'anonymous_user', 'rating', average_rating, 'date_created')
    list_filter = ('user', 'date_created')
    date_hierarchy = 'date_created'
    search_fields = ('user__username', 'feedback', 'rating')
    readonly_fields = ('date_created',)
    raw_id_fields = ('user',)
    resource_class = EmployeeFeedbackResource
    
    def get_export_queryset(self, request):
        return EmployeeFeedback.objects.filter(rating__gte=2)


class ColleagueFeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'feedback')
    list_filter = ('user',)
    search_fields = ('user__username', 'feedback')
    filter_horizontal = ('colleagues',)
    raw_id_fields = ('user',)


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title',)
    search_fields = ('title', 'description')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'questionnaire', 'anonymous_user')
    list_filter = ('user', 'questionnaire')
    search_fields = ('user__username', 'questionnaire__title', 'anonymous_user')


class AccessRightsAdmin(admin.ModelAdmin):
    list_display = ('user', 'questionnaire', 'can_view_answers')
    list_filter = ('user', 'questionnaire', 'can_view_answers')


class ManagerFeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'feedback')
    list_filter = ('user',)
    search_fields = ('user__username', 'feedback')


class SelfFeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'feedback')
    list_filter = ('user',)
    search_fields = ('user__username', 'feedback')


admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(AccessRights, AccessRightsAdmin)
admin.site.register(ManagerFeedback, ManagerFeedbackAdmin)
admin.site.register(SelfFeedback, SelfFeedbackAdmin)
admin.site.register(EmployeeFeedback, EmployeeFeedbackAdmin)
admin.site.register(ColleagueFeedback, ColleagueFeedbackAdmin)
