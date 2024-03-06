from import_export import resources
from import_export.fields import Field

from onlinerating.models import EmployeeFeedback


class EmployeeFeedbackResource(resources.ModelResource):
    full_name = Field(column_name="Full Name")
    feedback = Field(attribute="feedback", column_name="Feedback")
    anonymous_user = Field(attribute="anonymous_user", column_name="Anonymous User")
    rating = Field(attribute="rating", column_name="Rating")

    def dehydrate_full_name(self, obj: EmployeeFeedback):
        return f"{obj.user.first_name} {obj.user.last_name}"

    def dehydrate_rating(self, rate):
        return f"{rate.calculate_average_rating():.1f}"

    

    class Meta:
        model = EmployeeFeedback
        fields = ('date_created',)
