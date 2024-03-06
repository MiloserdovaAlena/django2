from django import forms
from .models import EmployeeFeedback, ManagerFeedback, SelfFeedback, ColleagueFeedback


class EmployeeFeedbackForm(forms.ModelForm):
    class Meta:
        model = EmployeeFeedback
        fields = ['user', 'anonymous_user', 'feedback', 'rating']


class ManagerFeedbackForm(forms.ModelForm):
    class Meta:
        model = ManagerFeedback
        fields = ['user', 'feedback']


class SelfFeedbackForm(forms.ModelForm):
    class Meta:
        model = SelfFeedback
        fields = ['feedback']


class ColleagueFeedbackForm(forms.ModelForm):
    class Meta:
        model = ColleagueFeedback
        fields = ['user', 'colleagues', 'feedback']
